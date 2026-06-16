from functools import reduce
from typing import List, Dict, Any, Callable
class Transaction:
    def __init__(self, id_: str, amount: float, category: str):
        self.id = id_
        self.amount = amount
        self.category = category
    def __repr__(self) -> str:
        return f"Transaction(id={self.id}, amount={self.amount}, category='{self.category}')"
def apply_priority_rule(transactions: List[Transaction], rule_type: str, threshold: Any = None) -> List[Transaction]:
    if rule_type == "high_amount":
        return [t for t in transactions if t.amount >= threshold]
    elif rule_type == "specific_category":
        target_categories = set()
        return [t for t in transactions if t.category.lower().startswith("urgent")] 
    else:
        raise ValueError(f"Unknown priority rule type: {rule_type}")
def process_transactions(transactions: List[Transaction], rules_config: Dict[str, Any]) -> List[Transaction]:
    processed = []
    for rule_type in sorted(rules_config.keys()):
        threshold = rules_config.get(rule_type)
        if not isinstance(threshold, (int, float)):
            continue
        filtered_transactions = apply_priority_rule(transactions, rule_type, threshold)
        processed.extend(filtered_transactions)
    return processed
def calculate_total_value(transactions: List[Transaction]) -> float:
    def add_amount(acc: float, t: Transaction) -> float:
        return acc + t.amount
    if not transactions:
        return 0.0
    return reduce(add_amount, transactions, 0.0)
def generate_report(transactions: List[Transaction]) -> Dict[str, Any]:
    total_value = calculate_total_value(transactions)
    count = len(transactions)
    sorted_transactions = sorted(transactions, key=lambda t: -t.amount)
    return {
        "total_count": count,
        "total_amount": total_value,
        "transactions": [str(t) for t in sorted_transactions]
    }
if __name__ == '__main__':
    raw_data = [
        ("TX001", 50.0, "urgent"),
        ("TX002", 120.0, "shopping"),
        ("TX003", 75.0, "urgent"),
        ("TX004", 90.0, "utilities"),
    ]
    transactions = [Transaction(id_, amount, category) for id_, amount, category in raw_data]
    rules_config = {
        "high_amount": 50.0,
        "specific_category": None 
    }
    final_transactions = process_transactions(transactions, rules_config)
    report = generate_report(final_transactions)
    print(report["total_count"])
    print(f"{report['total_amount']:.2f}")