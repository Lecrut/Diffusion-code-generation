class BooleanNegator:
    def __init__(self, value: bool):
        self.value = value

    def negate(self) -> bool:
        return not self.value

if __name__ == '__main__':
    negator_true = BooleanNegator(True)
    print(f"Negation of {negator_true.value}: {negator_true.negate()}")
    
    negator_false = BooleanNegator(False)
    print(f"Negation of {negator_false.value}: {negator_false.negate()}")