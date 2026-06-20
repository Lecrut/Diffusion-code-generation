class FloatingPointSum:
    PRECISION = 15

    @staticmethod
    def add_two_numbers(a, b):
        return round(a + b, FloatingPointSum.PRECISION)

if __name__ == '__main__':
    num1 = 3.141592653589793
    num2 = 2.718281828459045
    result = FloatingPointSum.add_two_numbers(num1, num2)
    print(result)