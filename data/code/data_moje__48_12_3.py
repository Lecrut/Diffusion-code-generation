class TransactionProcessor:
    def __init__(self, transactions):
        self.transactions = transactions

    def find_highest_transaction(self):
        max_value = None
        for sublist in self.transactions:
            for value in sublist:
                if max_value is None or value > max_value:
                    max_value = value
        return max_value

if __name__ == '__main__':
    hardcoded_transactions = [
        [100.50, 250.00, 15.75],
        [500.00, 320.25, 45.00],
        [1000.00, 750.50, 200.00]
    ]
    processor = TransactionProcessor(hardcoded_transactions)
    highest = processor.find_highest_transaction()
    print(highest)