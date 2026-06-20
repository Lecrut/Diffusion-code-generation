def process_transactions(transactions):
    filtered_transactions = [
        (account_id, amount)
        for account_id, amount in transactions
        if amount > 0 and account_id.startswith('A')
    ]
    return filtered_transactions

if __name__ == '__main__':
    sample_transactions = [
        ('A123', 100),
        ('B456', -50),
        ('A789', 200),
        ('C012', 150)
    ]
    print(process_transactions(sample_transactions))