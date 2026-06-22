class TransactionProcessor:
    def __init__(self, transactions):
        self.transactions = transactions

    def find_highest_transaction(self):
        max_value = float('-inf')
        for sublist in self.transactions:
            for amount in sublist:
                if amount > max_value:
                    max_value = amount
        return max_value

if __name__ == '__main__':
    hardcoded_transactions = [
        [100.50, 250.75, 300.00],
        [50.25, 150.00, 225.50],
        [300.00, 400.00, 100.00]
    ]
    processor = TransactionProcessor(hardcoded_transactions)
    print(processor.find_highest_transaction())