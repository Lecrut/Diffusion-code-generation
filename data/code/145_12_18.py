class FraudDetector:
    def __init__(self, amount_threshold=1000, frequency_threshold=3):
        self.amount_threshold = amount_threshold
        self.frequency_threshold = frequency_threshold

    def is_fraudulent(self, transactions):
        transaction_counts = {}
        for transaction in transactions:
            if transaction['amount'] > self.amount_threshold and \
               transaction['user_id'] not in transaction_counts:
                return True
            elif transaction['amount'] > self.amount_threshold:
                if transaction['user_id'] in transaction_counts:
                    transaction_counts[transaction['user_id']] += 1
                    if transaction_counts[transaction['user_id']] >= self.frequency_threshold:
                        return True
        return False

if __name__ == '__main__':
    detector = FraudDetector()
    transactions = [
        {'amount': 500, 'user_id': 'user1'},
        {'amount': 2000, 'user_id': 'user2'},
        {'amount': 1500, 'user_id': 'user3'},
        {'amount': 2500, 'user_id': 'user2'}
    ]
    result = detector.is_fraudulent(transactions)
    print(result)