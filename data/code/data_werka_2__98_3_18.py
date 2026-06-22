def validate_amount(amount):
    if not isinstance(amount, (int, float)):
        raise ValueError("Amount must be a number")
    return amount > 0

def validate_balance(balance, amount):
    if not isinstance(balance, (int, float)):
        raise ValueError("Balance must be a number")
    return balance >= amount

def validate_transaction_type(tx_type):
    if not isinstance(tx_type, str):
        raise ValueError("Transaction type must be a string")
    return tx_type == 'debit'

def approve_transaction(amount, balance, transaction_type):
    amount_ok = validate_amount(amount)
    balance_ok = validate_balance(balance, amount)
    type_ok = validate_transaction_type(transaction_type)
    if amount_ok and balance_ok and type_ok:
        return {"status": "approved", "remaining_balance": balance - amount}
    return {"status": "rejected", "remaining_balance": balance}

if __name__ == '__main__':
    result1 = approve_transaction(100, 500, 'debit')
    print(result1)
    result2 = approve_transaction(-50, 500, 'debit')
    print(result2)
    result3 = approve_transaction(200, 150, 'debit')
    print(result3)
    result4 = approve_transaction(100, 500, 'credit')
    print(result4)