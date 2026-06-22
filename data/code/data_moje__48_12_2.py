class TransactionProcessor:
    def __init__(self, transactions):
        self.transactions = transactions

    def get_highest_amount(self):
        max_val = None
        for sublist in self.transactions:
            for amount in sublist:
                if max_val is None or amount > max_val:
                    max_val = amount
        return max_val

if __name__ == '__main__':
    data = [
        [100.50, 200.75, 50.00],
        [300.00, 450.25, 120.00],
        [80.50, 950.00, 600.10]
    ]
    processor = TransactionProcessor(data)
    print(processor.get_highest_amount())