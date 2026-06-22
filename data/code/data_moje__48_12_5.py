class TransactionProcessor:
    def __init__(self, transactions):
        self.transactions = transactions

    def find_highest_transaction(self):
        if not self.transactions:
            return None
        highest = None
        for sublist in self.transactions:
            for amount in sublist:
                if highest is None or amount > highest:
                    highest = amount
        return highest

if __name__ == '__main__':
    transactions = [
        [100, 200, 150],
        [300, 50, 250],
        [175, 400, 125]
    ]
    processor = TransactionProcessor(transactions)
    result = processor.find_highest_transaction()
    print(result)