class DualFalseValidator:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def evaluate(self):
        return not bool(self.a) and not bool(self.b)

    def get_status(self):
        return "False" if self.evaluate() else "True"

if __name__ == '__main__':
    validator = DualFalseValidator(0, "")
    print(validator.evaluate())
    print(validator.get_status())