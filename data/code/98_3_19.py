VALIDATION_TYPES = {
    'debit': 'debit',
    'credit': 'credit',
    'transfer': 'transfer'
}

def validate_transaction(amount, balance, transaction_type):
    if transaction_type not in VALIDATION_TYPES:
        raise ValueError(f"Unsupported transaction type: {transaction_type}")
    
    is_positive_amount = amount > 0
    has_sufficient_funds = balance >= amount
    is_valid_type = transaction_type == 'debit'
    
    if is_positive_amount and has_sufficient_funds and is_valid_type:
        return {
            'status': 'approved',
            'remaining_balance': balance - amount,
            'amount_processed': amount
        }
    else:
        return {
            'status': 'rejected',
            'reason': 'insufficient_funds' if not has_sufficient_funds else 'invalid_amount_or_type',
            'remaining_balance': balance
        }

if __name__ == '__main__':
    sample_amount = 150
    sample_balance = 500
    sample_type = 'debit'
    
    result = validate_transaction(sample_amount, sample_balance, sample_type)
    print(result)