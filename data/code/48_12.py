class TransactionProcessor:
    def __init__(self, transactions):
        self.transactions = transactions

    def find_highest_value(self):
        max_value = float('-inf')
        for sublist in self.transactions:
            for amount in sublist:
                if amount > max_value:
                    max_value = amount
        return max_value

if __name__ == '__main__':
    transactions_data = [
        [100, 200, 50],
        [300, 450, 10],
        [500, 25, 60]
    ]

    processor = TransactionProcessor(transactions_data)
    result = processor.find_highest_value()
    print(result)