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
class DecisionEngine:
    def __init__(self):
        self._rules = []
    def add_rule(self, priority: int, condition_fn: Callable[[List[Transaction]], bool], action_fn: Callable[[List[Transaction]], List[Transaction]]):
        self._rules.append((priority, condition_fn, action_fn))
    def process_transactions(self, transactions: List[Transaction]) -> List[Transaction]:
        sorted_rules = sorted(self._rules, key=lambda x: x[0], reverse=True)
        current_list = [t for t in transactions]
        for _, condition_fn, action_fn in sorted_rules:
            if condition_fn(current_list):
                next_list = reduce(action_fn, list(reversed(range(len(current_list)))), current_list[:])                               
            new_transactions = []
        return transactions
def apply_rules(transactions: List[Transaction], rules_config: Dict[int, tuple]):
    def condition_fn(data):
        high_value = [t for t in data if t.amount > 100]
        return len(high_value) >= 2
    def action_fn(transactions_list):
        flagged = []
        for i, tx in enumerate(transactions_list):
            if condition_fn([tx]):
                flag_type = "HIGH_VALUE"
            else:
                flag_type = "NORMAL"
            if tx.amount > 100:
                flagged.append(tx)
        return flagged
    result = transactions
    priority_99 = (99, condition_fn, action_fn)
    final_result = reduce(lambda acc, item: [t for t in acc if not (item[1](acc))] or item[2], 
                         [(priority_99)], result)
    return final_result
def main():
    raw_data = [
        {"id": "TX001", "amount": 50.0, "category": "Food"},
        {"id": "TX002", "amount": 150.0, "category": "Travel"},
        {"id": "TX003", "amount": 75.0, "category": "Shopping"},
        {"id": "TX004", "amount": 200.0, "category": "Utilities"}
    ]
    transactions = parse_transactions(raw_data)
    engine = DecisionEngine()
    rules_config = {99: (lambda x: any(t.amount > 150 for t in x), lambda xs: [t for t in xs if t.amount > 150])}
    processed_transactions = apply_rules(transactions, rules_config)
    print(processed_transactions)
if __name__ == '__main__':
    main()