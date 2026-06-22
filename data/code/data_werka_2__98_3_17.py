class TransactionProcessor:
    def __init__(self, initial_balance):
        self.balance = initial_balance

    def check_approval(self, amount, transaction_type):
        is_positive = amount > 0
        has_sufficient_funds = self.balance >= amount
        is_debit = transaction_type == 'debit'
        return is_positive and has_sufficient_funds and is_debit

if __name__ == '__main__':
    processor = TransactionProcessor(1000)
    print(processor.check_approval(500, 'debit'))
    print(processor.check_approval(-100, 'debit'))
    print(processor.check_approval(1500, 'debit'))
    print(processor.check_approval(500, 'credit'))