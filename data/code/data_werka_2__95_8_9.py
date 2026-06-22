def validate_number(n):
    if not isinstance(n, (int, float)):
        raise ValueError("Input must be a number")
    if n <= 0:
        return "Not positive"
    if n % 2 != 0:
        return "Odd"
    if n >= 100:
        return "Too large"
    return "Positive, even, and less than 100"

class NumberValidator:
    def __init__(self, value):
        self.value = value

    def check(self):
        return validate_number(self.value)

if __name__ == '__main__':
    validator = NumberValidator(42)
    print(validator.check())
    
    validator2 = NumberValidator(-5)
    print(validator2.check())
    
    validator3 = NumberValidator(7)
    print(validator3.check())
    
    validator4 = NumberValidator(101)
    print(validator4.check())