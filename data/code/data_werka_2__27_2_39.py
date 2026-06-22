class ValueChecker:
    @staticmethod
    def are_values_different(a, b):
        return a != b

if __name__ == '__main__':
    a = 7
    b = 3
    print(ValueChecker.are_values_different(a, b))