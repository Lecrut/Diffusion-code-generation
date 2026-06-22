class TransactionProcessor:
    def __init__(self, transactions):
        self.transactions = transactions

    def find_max_transaction(self):
        max_val = None
        for sublist in self.transactions:
            for amount in sublist:
                if max_val is None or amount > max_val:
                    max_val = amount
        return max_val

if __name__ == '__main__':
    data = [
        [10, 20, 30],
        [5, 100, 15],
        [50, 25]
    ]
    processor = TransactionProcessor(data)
    result = processor.find_max_transaction()
    print(result)