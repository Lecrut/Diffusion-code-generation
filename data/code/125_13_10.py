class MathOperations:
    @staticmethod
    def calculate_sum_difference(a, b):
        return (a + b, a - b)

if __name__ == '__main__':
    num1 = 10
    num2 = 4
    result = MathOperations.calculate_sum_difference(num1, num2)
    print(result)