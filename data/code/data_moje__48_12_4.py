class TransactionProcessor:
    def __init__(self, data):
        self.data = data

    def get_highest_transaction(self):
        if not self.data or not any(self.data):
            raise ValueError("Transaction data cannot be empty")
        
        highest = float('-inf')
        for sublist in self.data:
            for amount in sublist:
                if amount > highest:
                    highest = amount
        return highest

if __name__ == '__main__':
    sample_data = [
        [100.50, 250.75, 50.25],
        [300.00, 150.99, 450.10],
        [200.00, 350.50, 100.00]
    ]
    processor = TransactionProcessor(sample_data)
    result = processor.get_highest_transaction()
    print(result)