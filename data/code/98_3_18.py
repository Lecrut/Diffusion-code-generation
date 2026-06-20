APPROVED = "Approved"
REJECTED = "Rejected"

def is_valid_transaction(amount, balance, transaction_type):
    if amount > 0 and balance >= amount and transaction_type == 'debit':
        return True
    else:
        return False

def process_transaction(amount, balance, transaction_type):
    if is_valid_transaction(amount, balance, transaction_type):
        return APPROVED
    else:
        return REJECTED

if __name__ == '__main__':
    transaction1_amount = 100
    transaction1_balance = 500
    transaction1_type = 'debit'
    result1 = process_transaction(transaction1_amount, transaction1_balance, transaction1_type)
    print(f"Transaction 1: {result1}")

    transaction2_amount = -50
    transaction2_balance = 500
    transaction2_type = 'debit'
    result2 = process_transaction(transaction2_amount, transaction2_balance, transaction2_type)
    print(f"Transaction 2: {result2}")

    transaction3_amount = 600
    transaction3_balance = 500
    transaction3_type = 'debit'
    result3 = process_transaction(transaction3_amount, transaction3_balance, transaction3_type)
    print(f"Transaction 3: {result3}")