def filter_transactions(transactions):
    return [t for t in transactions if t['amount'] > 0 and t['currency'] == 'USD']

if __name__ == '__main__':
    sample_transactions = [
        {'id': 1, 'amount': -50, 'currency': 'USD'},
        {'id': 2, 'amount': 300, 'currency': 'EUR'},
        {'id': 3, 'amount': 200, 'currency': 'USD'}
    ]
    filtered_transactions = filter_transactions(sample_transactions)
    print(filtered_transactions)