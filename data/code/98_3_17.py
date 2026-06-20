class TransactionProcessor:
    MIN_AMOUNT = 0

    @staticmethod
    def is_valid_transaction(amount, balance, transaction_type):
        return amount > TransactionProcessor.MIN_AMOUNT and balance >= amount and transaction_type == 'debit'

if __name__ == '__main__':
    processor = TransactionProcessor()
    transaction1_amount = 100
    transaction1_balance = 500
    transaction1_type = 'debit'
    result1 = processor.is_valid_transaction(transaction1_amount, transaction1_balance, transaction1_type)
    print(f"Transaction 1 Approved: {result1}")
    
    transaction2_amount = -50
    transaction2_balance = 500
    transaction2_type = 'debit'
    result2 = processor.is_valid_transaction(transaction2_amount, transaction2_balance, transaction2_type)
    print(f"Transaction 2 Approved: {result2}")

    transaction3_amount = 600
    transaction3_balance = 500
    transaction3_type = 'credit'
    result3 = processor.is_valid_transaction(transaction3_amount, transaction3_balance, transaction3_type)
    print(f"Transaction 3 Approved: {result3}")