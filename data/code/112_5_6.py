class NumberAdder:
    @staticmethod
    def sum_numbers(a, b):
        return a + b

if __name__ == '__main__':
    result = NumberAdder.sum_numbers(10, 5)
    print(result)