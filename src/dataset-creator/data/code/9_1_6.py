from typing import List, Callable, Dict, Any
class Transaction:
    def __init__(self, id: str, amount: float, category: str):
        self.id = id
        self.amount = amount
        self.category = category
def process_transaction(transaction: Transaction) -> bool:
    return transaction.amount > 0 and transaction.category in ["income", "expense"]
class DecisionEngine:
    def __init__(self, priority_rules: List[Callable[[Transaction], Any]]):
        self._rules = list(priority_rules)
    def make_decision(self, transactions: List[Transaction]) -> Dict[str, Transaction]:
        result: Dict[str, bool] = {}
        for transaction in transactions:
            if process_transaction(transaction):
                is_approved = False
                for rule in self._rules:
                    try:
                        condition_value = rule(transaction)
                        if isinstance(condition_value, bool):
                            is_approved = is_approved or condition_value
                        elif hasattr(condition_value, '__and__'):
                            pass
                    except Exception:
                        continue
                result[transaction.id] = transaction if is_approved else None
        return {k: v for k, v in result.items() if v is not None}
def main():
    transactions_data = [
        {"id": "T001", "amount": 50.0, "category": "income"},
        {"id": "T002", "amount": -30.0, "category": "expense"},
        {"id": "T003", "amount": 100.0, "category": "unknown"},
    ]
    transactions = [Transaction(**t) for t in transactions_data]
    priority_rules = []
    def rule_high_amount(t: Transaction) -> bool:
        return t.amount > 50
    def rule_valid_category(t: Transaction) -> bool:
        return t.category == "income" or t.category == "expense"
    priority_rules.append(rule_high_amount)
    priority_rules.append(rule_valid_category)
    engine = DecisionEngine(priority_rules=priority_rules)
    decisions = engine.make_decision(transactions=transactions)
    print(decisions)
if __name__ == '__main__':
    main()