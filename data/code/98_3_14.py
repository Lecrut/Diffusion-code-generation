def is_transaction_approved(amount, balance, transaction_type):
    return amount > 0 and balance >= amount and (transaction_type == 'debit')
if __name__ == '__main__':
    print(is_transaction_approved(50, 200, 'debit'))
    print(is_transaction_approved(-10, 200, 'debit'))
    print(is_transaction_approved(50, 30, 'debit'))
    print(is_transaction_approved(50, 200, 'credit'))