class NumberValidator:
    def __init__(self, value):
        self.value = value

    def is_valid(self):
        return self.value > 0 and self.value % 2 == 0 and self.value < 100

if __name__ == '__main__':
    validator = NumberValidator(42)
    print(validator.is_valid())
    print(validator.value)