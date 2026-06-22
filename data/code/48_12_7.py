class TransactionProcessor:
    def find_highest_transaction(self, transactions):
        if not transactions:
            raise ValueError("Transaction list cannot be empty")
        max_value = float('-inf')
        for sublist in transactions:
            for amount in sublist:
                if amount > max_value:
                    max_value = amount
        return max_value

if __name__ == '__main__':
    sample_transactions = [
        [100.50, 250.75, 50.00],
        [300.00, 150.25, 450.99],
        [75.50, 200.00, 1000.00],
        [-50.00, 125.75, 300.00]
    ]
    processor = TransactionProcessor()
    result = processor.find_highest_transaction(sample_transactions)
    print(result)