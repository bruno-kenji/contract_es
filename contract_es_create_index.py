from entities.contract import ContractService
from services.contract_es import ContractES

contract_service = ContractService()
contracts = contract_service.find({})
contract_es = ContractES()

for c in contracts:
    contract_es.update_index(c)
    print(c)
