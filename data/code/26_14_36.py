class NumberComparator:
    def __init__(self, num1, num2):
        if not isinstance(num1, int) or not isinstance(num2, int):
            raise ValueError("Both inputs must be integers.")
        self.num1 = num1
        self.num2 = num2

    def is_greater(self):
        return self.num1 > self.num2

if __name__ == '__main__':
    sample_num1 = 15
    sample_num2 = 9
    try:
        comparator = NumberComparator(sample_num1, sample_num2)
        result = comparator.is_greater()
        print(result)
    except ValueError as e:
        print(e)