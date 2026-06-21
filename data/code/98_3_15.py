class TransactionValidator:
    def __init__(self, initial_balance):
        self.current_balance = initial_balance

    def validate_debit(self, amount):
        amount_is_positive = amount > 0
        has_sufficient_funds = self.current_balance >= amount
        type_is_valid = True
        return amount_is_positive and has_sufficient_funds and type_is_valid

if __name__ == '__main__':
    validator = TransactionValidator(1000)
    approved_1 = validator.validate_debit(250)
    print(approved_1)
    approved_2 = validator.validate_debit(-10)
    print(approved_2)
    approved_3 = validator.validate_debit(1500)
    print(approved_3)