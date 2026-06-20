def is_transaction_approved(amount, balance, transaction_type):
    if amount > 0 and balance >= amount and transaction_type == 'debit':
        return True
    else:
        return False

if __name__ == '__main__':
    transaction1_amount = 150
    transaction1_balance = 750
    transaction1_type = 'debit'
    result1 = is_transaction_approved(transaction1_amount, transaction1_balance, transaction1_type)
    print(f"Transaction 1 Approved: {result1}")
    
    transaction2_amount = -50
    transaction2_balance = 750
    transaction2_type = 'debit'
    result2 = is_transaction_approved(transaction2_amount, transaction2_balance, transaction2_type)
    print(f"Transaction 2 Approved: {result2}")
    
    transaction3_amount = 100
    transaction3_balance = 150
    transaction3_type = 'debit'
    result3 = is_transaction_approved(transaction3_amount, transaction3_balance, transaction3_type)
    print(f"Transaction 3 Approved: {result3}")