class ValueChecker:
    @staticmethod
    def are_values_different(a, b):
        return a != b

if __name__ == '__main__':
    num1 = 42
    num2 = 24
    print(ValueChecker.are_values_different(num1, num2))