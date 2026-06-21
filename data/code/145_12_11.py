def filter_fraudulent_transactions(transactions):
    def is_fraudulent(transaction):
        amount_threshold = 500
        frequency_threshold = 3
        return transaction['amount'] > amount_threshold or transaction['frequency'] > frequency_threshold

    return [transaction for transaction in transactions if not is_fraudulent(transaction)]

if __name__ == '__main__':
    sample_transactions = [
        {'id': 1, 'amount': 200, 'frequency': 1},
        {'id': 2, 'amount': 600, 'frequency': 2},
        {'id': 3, 'amount': 400, 'frequency': 4}
    ]
    print(filter_fraudulent_transactions(sample_transactions))