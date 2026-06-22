def approve_transaction(amount, balance, transaction_type):
    if amount > 0 and transaction_type == 'debit' and balance >= amount:
        return True
    return False

if __name__ == '__main__':
    result = approve_transaction(100, 500, 'debit')
    print(result)