class NumberComparator:
    @staticmethod
    def compare(a, b):
        if a < b:
            return f"{a} is less than {b}"
        elif a > b:
            return f"{a} is greater than {b}"
        else:
            return f"{a} is equal to {b}"

if __name__ == '__main__':
    num1 = 5
    num2 = 10
    result = NumberComparator.compare(num1, num2)
    print(result)

    num3 = -3
    num4 = 7
    result2 = NumberComparator.compare(num3, num4)
    print(result2)

    num5 = 42
    num6 = 42
    result3 = NumberComparator.compare(num5, num6)
    print(result3)