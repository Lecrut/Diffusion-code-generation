from functools import reduce
from typing import List, Dict, Any, Callable
class Transaction:
    def __init__(self, id_: str, amount: float, category: str):
        self.id = id_
        self.amount = amount
        self.category = category
    def to_dict(self) -> Dict[str, Any]:
        return {"id": self.id, "amount": self.amount, "category": self.category}
def process_transactions(
    transactions: List[Transaction], 
    priority_rules: List[Callable[[Any], bool]],
    max_count: int = 0
) -> List[Dict[str, Any]]:
    def apply_rule(transaction: Transaction, rule: Callable[[Any], bool]) -> bool:
        return rule(transaction.to_dict())
    filtered_transactions = [t for t in transactions if any(apply_rule(t, r) for r in priority_rules)]
    sorted_transactions = reduce(lambda acc, item: (acc + ([item] if len(acc) < max_count else [])), 
                                reversed(filtered_transactions), [])[:max_count]
    return [t.to_dict() for t in sorted_transactions]
if __name__ == '__main__':
    transactions_data = [
        {"id": "T001", "amount": 50.0, "category": "Food"},
        {"id": "T002", "amount": 120.0, "category": "Travel"},
        {"id": "T003", "amount": 75.0, "category": "Food"},
    ]
    transactions = [Transaction(d["id"], d["amount"], d["category"]) for d in transactions_data]
    priority_rules = [lambda t: t["amount"] > 100, lambda t: t["category"] == "Travel"]
    result = process_transactions(transactions, priority_rules)
    print(result)