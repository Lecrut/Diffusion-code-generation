def filter_fraudulent_transactions(transactions):
    fraudulent = []
    for transaction in transactions:
        if transaction['amount'] > 1000 or (transaction['frequency'] > 3 and transaction['amount'] > 500):
            fraudulent.append(transaction)
    return fraudulent

if __name__ == '__main__':
    sample_transactions = [
        {'id': 1, 'amount': 200, 'frequency': 1},
        {'id': 2, 'amount': 1500, 'frequency': 1},
        {'id': 3, 'amount': 400, 'frequency': 4},
        {'id': 4, 'amount': 600, 'frequency': 2}
    ]
    print(filter_fraudulent_transactions(sample_transactions))