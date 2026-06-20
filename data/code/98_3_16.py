def process_transaction(amount, balance, transaction_type):
    if amount <= 0:
        raise ValueError("Amount must be positive")
    if balance < amount:
        raise ValueError("Insufficient balance")
    if transaction_type != 'debit':
        raise ValueError("Invalid transaction type. Only debits are allowed.")
    
    return True

if __name__ == '__main__':
    try:
        transaction1_amount = 100
        transaction1_balance = 500
        transaction1_type = 'debit'
        result1 = process_transaction(transaction1_amount, transaction1_balance, transaction1_type)
        print(f"Transaction 1 Approved: {result1}")
        
        transaction2_amount = -50
        transaction2_balance = 500
        transaction2_type = 'debit'
        result2 = process_transaction(transaction2_amount, transaction2_balance, transaction2_type)
    except ValueError as e:
        print(f"Transaction 2 Error: {e}")
    
    try:
        transaction3_amount = 600
        transaction3_balance = 500
        transaction3_type = 'debit'
        result3 = process_transaction(transaction3_amount, transaction3_balance, transaction3_type)
    except ValueError as e:
        print(f"Transaction 3 Error: {e}")