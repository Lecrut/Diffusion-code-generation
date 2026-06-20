def is_valid_transaction(amount, balance, transaction_type):
    if not isinstance(amount, (int, float)) or amount < 0:
        raise ValueError("Amount must be a non-negative number")
    if not isinstance(balance, (int, float)) or balance < 0:
        raise ValueError("Balance must be a non-negative number")
    if transaction_type != 'debit':
        raise ValueError("Transaction type must be 'debit'")
    return True

def process_transaction(amount, balance, transaction_type):
    try:
        is_valid_transaction(amount, balance, transaction_type)
        if amount > 0 and balance >= amount:
            return True
        else:
            return False
    except ValueError as e:
        print(f"Transaction Rejected: {e}")
        return False

if __name__ == '__main__':
    transaction1_amount = 100
    transaction1_balance = 500
    transaction1_type = 'debit'
    result1 = process_transaction(transaction1_amount, transaction1_balance, transaction1_type)
    print(f"Transaction 1 Approved: {result1}")
    
    transaction2_amount = -50
    transaction2_balance = 500
    transaction2_type = 'debit'
    result2 = process_transaction(transaction2_amount, transaction2_balance, transaction2_type)
    print(f"Transaction 2 Approved: {result2}")
    
    transaction3_amount = 600
    transaction3_balance = 500
    transaction3_type = 'debit'
    result3 = process_transaction(transaction3_amount, transaction3_balance, transaction3_type)
    print(f"Transaction 3 Approved: {result3}")