class TransactionProcessor:
    @staticmethod
    def find_highest_transaction(transactions):
        if not transactions:
            return None
        highest = transactions[0][0]
        for sublist in transactions:
            for amount in sublist:
                if amount > highest:
                    highest = amount
        return highest

if __name__ == '__main__':
    sample_transactions = [
        [100.50, 250.75, 300.00],
        [45.20, 999.99, 150.00],
        [200.00, 50.00, 750.25]
    ]
    processor = TransactionProcessor()
    print(processor.find_highest_transaction(sample_transactions))