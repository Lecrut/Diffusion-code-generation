class Summation:
    DEFAULT_VALUE = 0

    def __init__(self, value1=DEFAULT_VALUE, value2=DEFAULT_VALUE):
        self.value1 = value1
        self.value2 = value2

    @staticmethod
    def add(a, b):
        return a + b

    def calculate_sum(self):
        return Summation.add(self.value1, self.value2)

if __name__ == '__main__':
    first_number = 4
    second_number = 9
    summator = Summation(first_number, second_number)
    result = summator.calculate_sum()
    print(result)