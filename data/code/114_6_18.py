class Multiplication:
    VALUE1 = 8
    VALUE2 = 3

    @staticmethod
    def multiply(a, b):
        return a * b

if __name__ == '__main__':
    result = Multiplication.multiply(Multiplication.VALUE1, Multiplication.VALUE2)
    print(result)