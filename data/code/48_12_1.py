class TransactionProcessor:
    def __init__(self, transactions):
        self.transactions = transactions

    def get_highest_value(self):
        max_value = None
        for sublist in self.transactions:
            for amount in sublist:
                if max_value is None or amount > max_value:
                    max_value = amount
        return max_value

if __name__ == '__main__':
    hard_coded_transactions = [
        [100.5, 200.75, 50.0],
        [300.0, 150.25, 450.99],
        [50.0, 10.0, 75.5]
    ]
    processor = TransactionProcessor(hard_coded_transactions)
    print(processor.get_highest_value())