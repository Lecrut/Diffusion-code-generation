class TransactionProcessor:
    def __init__(self, transactions):
        self.transactions = transactions

    def get_highest_value(self):
        highest = float('-inf')
        for sublist in self.transactions:
            for amount in sublist:
                if amount > highest:
                    highest = amount
        return highest

if __name__ == '__main__':
    data = [
        [10.5, 20.0, -5.0],
        [100.0, 50.25, 75.0],
        [10.1, 200.5, 300.0]
    ]
    processor = TransactionProcessor(data)
    print(processor.get_highest_value())