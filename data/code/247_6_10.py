class NumberAdder:
    @staticmethod
    def add_numbers(a, b):
        return a + b

if __name__ == '__main__':
    num1 = 7
    num2 = 3
    result = NumberAdder.add_numbers(num1, num2)
    print(result)