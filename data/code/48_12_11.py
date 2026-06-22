class TransactionProcessor:
    def __init__(self):
        self.transactions = [
            [150.50, 200.75, 50.25],
            [300.00, 99.99, 450.50, 12.30],
            [5.00, 750.00, 200.00],
            [1000.00, 250.50, 30.00]
        ]

    def find_max_transaction(self):
        if not self.transactions:
            return 0.0
        max_value = self.transactions[0][0]
        for sublist in self.transactions:
            if not sublist:
                continue
            current_max = sublist[0]
            for amount in sublist:
                if amount > current_max:
                    current_max = amount
            if current_max > max_value:
                max_value = current_max
        return max_value

if __name__ == '__main__':
    processor = TransactionProcessor()
    result = processor.find_max_transaction()
    print(result)