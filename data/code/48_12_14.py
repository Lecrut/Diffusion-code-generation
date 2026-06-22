class TransactionProcessor:
    def __init__(self, transactions):
        self.transactions = transactions

    def find_max_transaction(self):
        max_value = float('-inf')
        for sublist in self.transactions:
            for amount in sublist:
                if amount > max_value:
                    max_value = amount
        return max_value

if __name__ == '__main__':
    sample_transactions = [
        [100.5, 200.75, 150.0],
        [300.25, 50.0, 125.5],
        [400.0, 75.25, 300.0]
    ]
    processor = TransactionProcessor(sample_transactions)
    print(processor.find_max_transaction())