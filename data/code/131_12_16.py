class TransactionProcessor:
    def __init__(self):
        self.rules = [
            {'condition': lambda t: t['amount'] > 100, 'result': 'High Value'},
            {'condition': lambda t: t['category'] == 'Groceries', 'result': 'Essential'},
            {'condition': lambda t: t['date'].weekday() == 5, 'result': 'Weekend'}
        ]

    def process_transactions(self, transactions):
        return [self.apply_rules(t) for t in transactions]

    def apply_rules(self, transaction):
        for rule in self.rules:
            if rule['condition'](transaction):
                return rule['result']
        return 'Standard'

if __name__ == '__main__':
    processor = TransactionProcessor()
    sample_transactions = [
        {'amount': 50, 'category': 'Groceries', 'date': datetime.datetime(2023, 10, 7)},
        {'amount': 150, 'category': 'Entertainment', 'date': datetime.datetime(2023, 10, 6)},
        {'amount': 80, 'category': 'Groceries', 'date': datetime.datetime(2023, 10, 5)}
    ]
    results = processor.process_transactions(sample_transactions)
    print(results)