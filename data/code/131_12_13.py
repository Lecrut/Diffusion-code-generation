def filter_transactions(transactions):
    return [t for t in transactions if t['amount'] > 0 and t['status'] == 'approved']

if __name__ == '__main__':
    sample_transactions = [
        {'id': 1, 'amount': -50, 'status': 'pending'},
        {'id': 2, 'amount': 100, 'status': 'approved'},
        {'id': 3, 'amount': 200, 'status': 'declined'},
        {'id': 4, 'amount': 50, 'status': 'approved'}
    ]
    filtered_transactions = filter_transactions(sample_transactions)
    print(filtered_transactions)