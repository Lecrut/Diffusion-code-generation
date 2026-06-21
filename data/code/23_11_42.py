class NumberComparison:
    @staticmethod
    def greater_of_two(a, b):
        return (a + b + abs(a - b)) // 2

if __name__ == '__main__':
    num1 = 50
    num2 = 30
    result = NumberComparison.greater_of_two(num1, num2)
    print(result)