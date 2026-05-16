class NumberComparator:
    @staticmethod
    def are_unequal(a, b):
        return a != b
if __name__ == '__main__':
    num1 = 10
    num2 = 5
    result1 = NumberComparator.are_unequal(num1, num2)
    print(f"Are {num1} and {num2} unequal? {result1}")
    num3 = 7
    num4 = 7
    result2 = NumberComparator.are_unequal(num3, num4)
    print(f"Are {num3} and {num4} unequal? {result2}")
    num5 = "hello"
    num6 = "world"
    result3 = NumberComparator.are_unequal(num5, num6)
    print(f"Are '{num5}' and '{num6}' unequal? {result3}")