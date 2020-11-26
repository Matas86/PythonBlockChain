from bitcoin.rpc import RawProxy
import sys

p = RawProxy()

# Get transactions ID from input
txid = sys.argv[1]

# First, retrieve the raw transaction in hex
raw_tx = p.getrawtransaction(txid)

# Decode the transaction hex into a JSON object
decoded_tx = p.decoderawtransaction(raw_tx)

outputValue=0

# Retrieve each of the outputs from the transaction
for output in decoded_tx['vout']:
    outputValue+=output['value']

inputValue=0
#search for inputs and add the correct ones to inputValue
for input in decoded_tx['vin']:
    r_tx=p.getrawtransaction(input['txid'])
    readable_tx=p.decoderawtransaction(r_tx)
    voutas=input['vout']

    for transakcija in readable_tx['vout']:
        if transakcija['n']==voutas:
            txInputValue=transakcija
    inputValue+=txInputValue['value']
    
#calculate and print transaction free
print("Transaction Fee:{} BTC ").format(inputValue-outputValue)
