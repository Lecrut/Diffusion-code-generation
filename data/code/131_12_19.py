def filter_transactions(transactions):
    filtered = [
        t for t in transactions if t['amount'] > 0 and t['status'] == 'approved'
    ]
    return filtered

if __name__ == '__main__':
    sample_transactions = [
        {'id': 1, 'amount': -20, 'status': 'pending'},
        {'id': 2, 'amount': 30, 'status': 'approved'},
        {'id': 3, 'amount': 50, 'status': 'declined'},
        {'id': 4, 'amount': 10, 'status': 'approved'}
    ]
    result = filter_transactions(sample_transactions)
    print(result)