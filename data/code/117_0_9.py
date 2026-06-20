class MathOperations:
    @staticmethod
    def calculate_difference(num1, num2):
        return num1 - num2

if __name__ == '__main__':
    num1 = 15
    num2 = 7
    difference = MathOperations.calculate_difference(num1, num2)
    print(difference)