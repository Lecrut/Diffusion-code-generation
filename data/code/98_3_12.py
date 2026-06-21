def approve_transaction(amount, balance, transaction_type):
    if amount <= 0:
        return False
    if transaction_type != 'debit':
        return False
    if amount > balance:
        return False
    return True

if __name__ == '__main__':
    result = approve_transaction(100, 500, 'debit')
    print(result)