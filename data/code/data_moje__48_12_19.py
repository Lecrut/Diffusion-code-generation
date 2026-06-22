class TransactionProcessor:
    def __init__(self, transactions):
        self.transactions = transactions

    def get_highest_value(self):
        max_value = float('-inf')
        for row in self.transactions:
            for amount in row:
                if amount > max_value:
                    max_value = amount
        return max_value

if __name__ == '__main__':
    data = [
        [100, 200, 300],
        [150, 250, 350],
        [400, 500, 600]
    ]
    processor = TransactionProcessor(data)
    print(processor.get_highest_value())