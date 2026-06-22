class TransactionProcessor:
    def __init__(self, transactions):
        self.transactions = transactions

    def find_highest_value(self):
        if not self.transactions:
            return None
        max_value = float('-inf')
        for sublist in self.transactions:
            for amount in sublist:
                if amount > max_value:
                    max_value = amount
        return max_value

if __name__ == '__main__':
    sample_data = [
        [10, 25, 30],
        [45, 5, 100],
        [20, 85, 15]
    ]
    processor = TransactionProcessor(sample_data)
    print(processor.find_highest_value())