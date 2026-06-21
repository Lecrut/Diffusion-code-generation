def filter_fraudulent_transactions(transactions):
    thresholds = {
        'amount': 1000,
        'frequency': 5
    }
    
    def is_fraudulent(transaction):
        if transaction['amount'] > thresholds['amount']:
            return True
        if transaction['frequency'] > thresholds['frequency']:
            return True
        return False
    
    fraudulent_transactions = [t for t in transactions if is_fraudulent(t)]
    return fraudulent_transactions

if __name__ == '__main__':
    sample_transactions = [
        {'id': 1, 'amount': 500, 'frequency': 3},
        {'id': 2, 'amount': 1500, 'frequency': 4},
        {'id': 3, 'amount': 800, 'frequency': 6},
        {'id': 4, 'amount': 1200, 'frequency': 2}
    ]
    
    fraudulent = filter_fraudulent_transactions(sample_transactions)
    print(fraudulent)