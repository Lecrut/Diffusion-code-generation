def process_transaction(amount, balance, transaction_type):
    if amount > 0 and balance >= amount and transaction_type == 'debit':
        return "Approved"
    else:
        return "Rejected"
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
    transaction3_amount = 200
    transaction3_balance = 150
    transaction3_type = 'debit'
    result3 = process_transaction(transaction3_amount, transaction3_balance, transaction3_type)
    print(f"Transaction 3: {result3}")
    transaction4_amount = 100
    transaction4_balance = 500
    transaction4_type = 'credit'
    result4 = process_transaction(transaction4_amount, transaction4_balance, transaction4_type)
    print(f"Transaction 4: {result4}")
    transaction5_amount = 0
    transaction5_balance = 1000
    transaction5_type = 'debit'
    result5 = process_transaction(transaction5_amount, transaction5_balance, transaction5_type)
    print(f"Transaction 5: {result5}")