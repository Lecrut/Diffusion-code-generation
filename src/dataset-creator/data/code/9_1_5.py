from functools import reduce
from typing import List, Dict, Any
class Transaction:
    def __init__(self, id_: str, amount: float, category: str):
        self.id = id_
        self.amount = amount
        self.category = category
    def to_dict(self) -> Dict[str, Any]:
        return {"id": self.id, "amount": self.amount, "category": self.category}
def parse_transactions(data: List[Dict[str, Any]]) -> List[Transaction]:
    return [Transaction(d["id"], d["amount"], d["category"]) for d in data]
def apply_priority_rules(transactions: List[Transaction], rules: Dict[int, str]) -> List[Transaction]:
    def sort_key(t):
        priority = 0
        if t.category == "high":
            priority += int(rules.get(1, 9))
        elif t.category == "medium":
            priority += int(rules.get(2, 5))
        else:
            priority += int(rules.get(3, 1))
        return (-priority, -t.amount)
    sorted_transactions = sorted(transactions, key=sort_key)
    def filter_by_limit(t):
        if t.category == "high":
            limit = rules.get(4, float('inf'))
            return True if t.amount <= limit else False
        elif t.category == "medium":
            limit = rules.get(5, 100)
            return True if t.amount <= limit else False
        else:
            limit = rules.get(6, 200)
            return True if t.amount <= limit else False
    filtered_transactions = [t for t in sorted_transactions if filter_by_limit(t)]
    def select_top_n(transactions):
        n = int(rules.get(7, len(transactions)))
        return transactions[:n]
    final_result = list(select_top_n(filtered_transactions))
    return final_result
def process_transaction_list(data: List[Dict[str, Any]], rules_config: Dict[int, str]) -> List[Transaction]:
    raw_data = parse_transactions(data)
    processed_data = apply_priority_rules(raw_data, rules_config)
    result = [t.to_dict() for t in processed_data]
    return result
if __name__ == '__main__':
    sample_data = [
        {"id": "T001", "amount": 50.0, "category": "high"},
        {"id": "T002", "amount": 30.0, "category": "medium"},
        {"id": "T003", "amount": 80.0, "category": "low"},
        {"id": "T004", "amount": 15.0, "category": "high"},
    ]
    rules = {
        1: 9, 
        2: 5, 
        3: 1, 
        4: float('inf'), 
        5: 60, 
        6: 80, 
        7: len(sample_data) - 1
    }
    output = process_transaction_list(sample_data, rules)
    print(output)