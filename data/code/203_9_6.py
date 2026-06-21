class NumberComparer:
    TOLERANCE = 1e-9

    @staticmethod
    def are_close(num1, num2):
        return abs(num1 - num2) <= NumberComparer.TOLERANCE

if __name__ == '__main__':
    result = NumberComparer.are_close(0.1 + 0.2, 0.3)
    print(result)