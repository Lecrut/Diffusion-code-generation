def filter_fraudulent_transactions(transactions):
    def is_suspicious(transaction):
        return transaction['amount'] > 1000 or transaction['frequency'] > 5

    return [transaction for transaction in transactions if not is_suspicious(transaction)]

if __name__ == '__main__':
    sample_transactions = [
        {'id': 1, 'amount': 200, 'frequency': 3},
        {'id': 2, 'amount': 1500, 'frequency': 4},
        {'id': 3, 'amount': 800, 'frequency': 6}
    ]
    print(filter_fraudulent_transactions(sample_transactions))