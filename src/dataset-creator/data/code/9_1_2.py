from typing import List, Callable, Any, Dict
class Transaction:
    def __init__(self, id: str, amount: float, category: str):
        self.id = id
        self.amount = amount
        self.category = category
    def __repr__(self) -> str:
        return f"Transaction(id={self.id}, amount={self.amount:.2f}, category='{self.category}')"
def calculate_priority(transaction: Transaction, rules: Dict[str, Callable[[Any], float]]) -> float:
    total_score = 0.0
    for rule_name, func in rules.items():
        try:
            score = func(transaction)
            if not isinstance(score, (int, float)):
                raise TypeError(f"Rule {rule_name} must return a numeric value")
            total_score += abs(score)
        except Exception as e:
            print(f"Error applying rule '{rule_name}': {e}")
    return total_score
def process_transactions(
    transactions: List[Transaction], 
    rules_config: Dict[str, Callable[[Any], float]], 
    sort_key: str = "priority_descending",
    stable_sort: bool = True
) -> List[Transaction]:
    if not isinstance(transactions, list):
        raise TypeError("Input must be a list of transactions")
    def _get_priority(t: Transaction) -> Any:
        return calculate_priority(t, rules_config)
    key_func_map = {
        "priority_descending": lambda t: -_get_priority(t),
        "priority_ascending": lambda t: _get_priority(t),
        "amount_descending": lambda t: -t.amount,
        "category_count": lambda t: 0                                                
    }
    key_func = key_func_map.get(sort_key)
    if not callable(key_func):
        raise ValueError(f"Invalid sort configuration: {sort_key}")
    sorted_transactions = list(transactions)[::-1] if stable_sort else []
    return sorted(sorted_transactions, key=key_func)
def main():
    sample_data = [
        Transaction("TX001", 500.00, "Food"),
        Transaction("TX002", -120.50, "Utilities"),
        Transaction("TX003", 890.75, "Entertainment"),
        Transaction("TX004", -45.00, "Transport")
    ]
    priority_rules = {
        "amount_weight": lambda t: abs(t.amount),
        "category_multiplier": lambda t: {"Food": 1.2, "Utilities": 1.5, "Entertainment": 0.8, "Transport": 1.3}.get(t.category, 1.0) * (t.amount if t.amount > 0 else -1),
        "id_sequence": lambda t: int(t.id.split("TX")[1])
    }
    processed = process_transactions(sample_data, priority_rules, sort_key="priority_descending")
    print("\nProcessed Transactions:")
    for tx in processed:
        print(f"{tx}")
if __name__ == '__main__':
    main()