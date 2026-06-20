class Multiplier:
    @staticmethod
    def multiply(a, b):
        return a * b

if __name__ == '__main__':
    result = Multiplier.multiply(4, 3)
    print(result)