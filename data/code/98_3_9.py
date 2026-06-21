def evaluate_transaction(amount, current_balance, transaction_type):
    is_positive = amount > 0
    has_sufficient_funds = current_balance >= amount
    is_debit = transaction_type == 'debit'
    is_valid = is_positive and has_sufficient_funds and is_debit
    return is_valid

if __name__ == '__main__':
    sample_amount = 250
    sample_balance = 300
    sample_type = 'debit'
    outcome = evaluate_transaction(sample_amount, sample_balance, sample_type)
    print(outcome)