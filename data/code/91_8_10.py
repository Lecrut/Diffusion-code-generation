class BooleanNegator:
    def __init__(self, value):
        self.value = value

    def negate(self):
        return not self.value

if __name__ == '__main__':
    negator_true = BooleanNegator(True)
    print(f"Original: {negator_true.value}, Negated: {negator_true.negate()}")
    
    negator_false = BooleanNegator(False)
    print(f"Original: {negator_false.value}, Negated: {negator_false.negate()}")