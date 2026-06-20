class NumberReverser:
    @staticmethod
    def reverse_numbers(a, b):
        a = a + b - (b := a)
        return a, b

if __name__ == '__main__':
    num1 = 20
    num2 = 35
    result = NumberReverser.reverse_numbers(num1, num2)
    print(result)