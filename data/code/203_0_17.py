class NumberComparer:
    GREATER = "Greater"
    LESSER = "Lesser"
    EQUAL = "Equal"

    @staticmethod
    def compare(a, b):
        if a > b:
            return NumberComparer.GREATER
        elif a < b:
            return NumberComparer.LESSER
        else:
            return NumberComparer.EQUAL

if __name__ == '__main__':
    num1 = 5
    num2 = 3
    result = NumberComparer.compare(num1, num2)
    print(result)