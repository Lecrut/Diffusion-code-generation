def is_transaction_approved(amount, balance, transaction_type):
    return amount > 0 and balance >= amount and (transaction_type == 'debit')
if __name__ == '__main__':
    print(is_transaction_approved(100, 500, 'debit'))
    print(is_transaction_approved(-50, 500, 'debit'))
    print(is_transaction_approved(200, 150, 'debit'))
    print(is_transaction_approved(100, 500, 'credit'))