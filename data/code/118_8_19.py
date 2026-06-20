class Multiplier:
    @classmethod
    def multiply(cls, a, b):
        return a * b

if __name__ == '__main__':
    num1 = 5
    num2 = 3
    result = Multiplier.multiply(num1, num2)
    print(result)