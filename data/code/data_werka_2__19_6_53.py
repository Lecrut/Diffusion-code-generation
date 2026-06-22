class NumberValidator:
    @staticmethod
    def validate(value):
        if not isinstance(value, int):
            raise ValueError(f"Invalid input: {value} is not an integer.")
        return value

class Comparator:
    def __init__(self, num1, num2):
        self.num1 = NumberValidator.validate(num1)
        self.num2 = NumberValidator.validate(num2)

    def is_strictly_greater(self):
        return self.num1 > self.num2

if __name__ == '__main__':
    try:
        sample_values = [(10, 5), (3, 7)]
        for value1, value2 in sample_values:
            comparator = Comparator(value1, value2)
            print(comparator.is_strictly_greater())
    except ValueError as e:
        print(e)