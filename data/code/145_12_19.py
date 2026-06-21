def is_fraudulent(transaction):
    amount_threshold = 1000
    frequency_threshold = 3
    
    def check_amount(amount):
        return amount > amount_threshold
    
    def check_frequency(frequency):
        return frequency >= frequency_threshold
    
    if transaction['amount'] < amount_threshold:
        return False
    
    recent_transactions = [t for t in transactions if t['user_id'] == transaction['user_id']]
    frequency = sum(1 for t in recent_transactions if abs(t['timestamp'] - transaction['timestamp']) <= 24*3600)
    
    return check_frequency(frequency)

def filter_fraudulent(transactions):
    return [t for t in transactions if is_fraudulent(t)]

if __name__ == '__main__':
    transactions = [
        {'user_id': '1', 'amount': 500, 'timestamp': 1633072800},
        {'user_id': '1', 'amount': 1500, 'timestamp': 1633072900},
        {'user_id': '1', 'amount': 2000, 'timestamp': 1633073000},
        {'user_id': '2', 'amount': 100, 'timestamp': 1633072800}
    ]
    
    fraudulent_transactions = filter_fraudulent(transactions)
    print(fraudulent_transactions)