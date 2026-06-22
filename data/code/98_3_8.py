def approve_transaction(amount, balance, transaction_type):
    if amount > 0 and transaction_type == 'debit' and amount <= balance:
        return True
    return False

if __name__ == '__main__':
    amount = 100
    balance = 500
    transaction_type = 'debit'
    result = approve_transaction(amount, balance, transaction_type)
    print(result)