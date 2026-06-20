class NumericAdder:
    DEFAULT_NUM1 = 0
    DEFAULT_NUM2 = 0

    @staticmethod
    def add_numbers(num1=DEFAULT_NUM1, num2=DEFAULT_NUM2):
        return num1 + num2

if __name__ == '__main__':
    result = NumericAdder.add_numbers(10, 5)
    print(result)