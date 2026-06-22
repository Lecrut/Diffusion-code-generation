class TransactionProcessor:
    def __init__(self, transactions):
        self.transactions = transactions

    def find_highest_transaction(self):
        highest = None
        for sublist in self.transactions:
            for amount in sublist:
                if highest is None or amount > highest:
                    highest = amount
        return highest

if __name__ == '__main__':
    sample_transactions = [
        [100.50, 250.75, 300.00],
        [50.25, 150.00, 200.50],
        [75.00, 300.25, 100.00]
    ]
    processor = TransactionProcessor(sample_transactions)
    highest_value = processor.find_highest_transaction()
    print(highest_value)