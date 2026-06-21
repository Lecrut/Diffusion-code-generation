def filter_fraudulent_transactions(transactions, amount_threshold=500, frequency_threshold=3):
    def is_fraudulent(transaction):
        return transaction['amount'] > amount_threshold and transaction['frequency'] >= frequency_threshold

    return [transaction for transaction in transactions if is_fraudulent(transaction)]

if __name__ == '__main__':
    sample_transactions = [
        {'id': 1, 'amount': 600, 'frequency': 2},
        {'id': 2, 'amount': 450, 'frequency': 3},
        {'id': 3, 'amount': 700, 'frequency': 1}
    ]
    fraudulent_transactions = filter_fraudulent_transactions(sample_transactions)
    print(fraudulent_transactions)