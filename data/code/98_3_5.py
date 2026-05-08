def process_transaction(amount, balance, transaction_type):
    if amount > 0 and balance >= amount and transaction_type == 'debit':
        return True
    else:
        return False
if __name__ == '__main__':
    transaction_amount = 100
    user_balance = 500
    transaction_type = 'debit'
    result = process_transaction(transaction_amount, user_balance, transaction_type)
    print(result)