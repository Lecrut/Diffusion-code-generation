def validate_amount(amount):
    if not isinstance(amount, (int, float)):
        raise ValueError("Amount must be a number")
    if amount <= 0:
        raise ValueError("Amount must be positive")
    return True

def validate_balance(balance, amount):
    if not isinstance(balance, (int, float)):
        raise ValueError("Balance must be a number")
    if balance < amount:
        raise ValueError("Insufficient balance")
    return True

def process_transaction(amount, balance, transaction_type):
    validate_amount(amount)
    validate_balance(balance, amount)
    if transaction_type == 'debit':
        return True
    return False

if __name__ == '__main__':
    result1 = process_transaction(100, 500, 'debit')
    print(result1)
    result2 = process_transaction(-50, 500, 'debit')
    print(result2)
    result3 = process_transaction(200, 150, 'debit')
    print(result3)
    result4 = process_transaction(100, 500, 'credit')
    print(result4)