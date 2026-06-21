class NumberComparator:
    def __init__(self, num1, num2):
        self.num1 = self.validate_integer(num1)
        self.num2 = self.validate_integer(num2)

    @staticmethod
    def validate_integer(value):
        if not isinstance(value, int):
            raise ValueError("Input must be an integer")
        return value

    def is_strictly_greater(self):
        return self.num1 > self.num2

if __name__ == '__main__':
    try:
        comparator = NumberComparator(10, 5)
        print(comparator.is_strictly_greater())
        comparator = NumberComparator(3, 7)
        print(comparator.is_strictly_greater())
    except ValueError as e:
        print(e)