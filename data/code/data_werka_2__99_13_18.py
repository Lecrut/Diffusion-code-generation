class StateValidator:
    def __init__(self, a: bool, b: bool, c: bool, d: bool):
        self.a = a
        self.b = b
        self.c = c
        self.d = d

    def evaluate(self) -> bool:
        if self.a:
            return self.b
        if self.c:
            return not self.d
        return self.a or self.b or self.c or self.d

if __name__ == '__main__':
    validator = StateValidator(True, False, False, True)
    print(validator.evaluate())
    
    validator2 = StateValidator(False, False, True, False)
    print(validator2.evaluate())
    
    validator3 = StateValidator(False, False, False, False)
    print(validator3.evaluate())