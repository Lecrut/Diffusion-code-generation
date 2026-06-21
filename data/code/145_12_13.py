def filter_fraudulent_transactions(transactions):
    def is_suspicious(transaction):
        return transaction['amount'] > 1000 or transaction['frequency'] > 5

    def is_fraudulent(transaction):
        return is_suspicious(transaction) and 'fraud' in transaction.get('tags', [])

    return [transaction for transaction in transactions if not is_fraudulent(transaction)]

if __name__ == '__main__':
    sample_transactions = [
        {'amount': 200, 'frequency': 3, 'tags': []},
        {'amount': 1500, 'frequency': 4, 'tags': ['suspicious']},
        {'amount': 500, 'frequency': 6, 'tags': ['fraud']},
        {'amount': 800, 'frequency': 2, 'tags': []}
    ]
    print(filter_fraudulent_transactions(sample_transactions))