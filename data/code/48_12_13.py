class TransactionProcessor:
    def __init__(self, data):
        self.data = data

    def get_highest_transaction(self):
        if not self.data:
            return None
        max_value = None
        for sublist in self.data:
            if not sublist:
                continue
            current_max = sublist[0]
            for value in sublist[1:]:
                if value > current_max:
                    current_max = value
            if max_value is None or current_max > max_value:
                max_value = current_max
        return max_value

if __name__ == '__main__':
    sample_transactions = [
        [100, 250, 75],
        [500, 300, 150, 600],
        [200, 400],
        [50, 900, 100]
    ]
    processor = TransactionProcessor(sample_transactions)
    print(processor.get_highest_transaction())