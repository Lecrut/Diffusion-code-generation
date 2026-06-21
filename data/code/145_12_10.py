def filter_fraudulent_transactions(transactions):
    def is_fraudulent(transaction):
        amount = transaction['amount']
        frequency = transaction['frequency']
        return (amount > 1000) or (frequency > 5)

    return [transaction for transaction in transactions if is_fraudulent(transaction)]

if __name__ == '__main__':
    sample_transactions = [
        {'amount': 200, 'frequency': 3},
        {'amount': 1500, 'frequency': 4},
        {'amount': 800, 'frequency': 6}
    ]
    print(filter_fraudulent_transactions(sample_transactions))