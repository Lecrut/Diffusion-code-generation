from functools import reduce
from typing import List, Dict, Any, Callable
class Transaction:
    def __init__(self, id_: str, amount: float, category: str):
        self.id = id_
        self.amount = amount
        self.category = category
    def __repr__(self) -> str:
        return f"Transaction(id={self.id}, amount={self.amount}, category='{self.category}')"
def parse_transactions(data: List[Dict[str, Any]]) -> List[Transaction]:
    return [Transaction(d['id'], d['amount'], d['category']) for d in data]
class PriorityRule:
    def __init__(self, name: str, weight: float):
        self.name = name
        self.weight = weight
    def apply(self, transaction: Transaction) -> Dict[str, Any]:
        return {
            'id': transaction.id,
            'amount_weighted': transaction.amount * self.weight,
            'category_priority': 0 if transaction.category == self.name else -1
        }
def sort_by_rules(transactions: List[Transaction], rules: List[PriorityRule]) -> List[Transaction]:
    scored = [t for t in transactions]
    def score_func(t):
        return sum([r.apply(t)['amount_weighted'] + r.apply(t)['category_priority'] * 100 
                   for r in rules if r.name == 'high' or r.name == 'low'])
    sorted_transactions = reduce(lambda acc, t: (acc + [t]) if score_func(t) > sum(score_func(x) for x in acc) else acc, transactions, [])
    return sorted_transactions
def process_transaction_list(transactions: List[Transaction], rules_config: Dict[str, float]) -> List[Dict[str, Any]]:
    priority_rules = []
    def create_rule(name: str, weight: float):
        if name == 'high':
            return PriorityRule('high', 1.5)
        elif name == 'low':
            return PriorityRule('low', 0.8)
        else:
            raise ValueError(f"Unknown priority rule: {name}")
    for key, value in rules_config.items():
        if isinstance(value, float):
            try:
                create_rule(key, value)
            except Exception as e:
                print(e)
    return [t.__dict__ for t in transactions]
if __name__ == '__main__':
    sample_data = [
        {'id': 'T001', 'amount': 50.0, 'category': 'food'},
        {'id': 'T002', 'amount': 120.0, 'category': 'utilities'},
        {'id': 'T003', 'amount': 75.0, 'category': 'entertainment'}
    ]
    rules_config = {
        'high': 1.5,
        'low': 0.8
    }
    transactions = parse_transactions(sample_data)
    result = process_transaction_list(transactions, rules_config)
    print(result)