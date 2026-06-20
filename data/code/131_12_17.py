def filter_transactions(transactions):
    return [t for t in transactions if t['amount'] > 0 and t['type'] == 'credit']

if __name__ == '__main__':
    sample_transactions = [
        {'id': 1, 'amount': -50, 'type': 'debit'},
        {'id': 2, 'amount': 300, 'type': 'credit'},
        {'id': 3, 'amount': 200, 'type': 'credit'},
        {'id': 4, 'amount': -100, 'type': 'debit'}
    ]
    filtered_transactions = filter_transactions(sample_transactions)
    print(filtered_transactions)