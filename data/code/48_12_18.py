class TransactionProcessor:
    def __init__(self, data):
        self.data = data

    def get_max_transaction(self):
        max_value = None
        for row in self.data:
            for value in row:
                if max_value is None or value > max_value:
                    max_value = value
        return max_value

if __name__ == '__main__':
    transactions = [
        [100, 250, 75],
        [300, 150, 400],
        [50, 500, 125],
        [200, 350, 100]
    ]
    processor = TransactionProcessor(transactions)
    print(processor.get_max_transaction())