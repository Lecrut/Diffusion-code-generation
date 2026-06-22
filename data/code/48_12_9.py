class TransactionProcessor:
    def __init__(self, transactions):
        self.transactions = transactions

    def find_highest_amount(self):
        max_value = None
        for sublist in self.transactions:
            for amount in sublist:
                if max_value is None or amount > max_value:
                    max_value = amount
        return max_value

if __name__ == '__main__':
    sample_transactions = [
        [100.50, 200.75, 50.00],
        [300.25, 45.60],
        [999.99, 10.05, 500.00]
    ]
    processor = TransactionProcessor(sample_transactions)
    result = processor.find_highest_amount()
    print(result)