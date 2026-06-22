class NumberAdder:
    @staticmethod
    def add_numbers(a, b):
        return a + b

if __name__ == '__main__':
    result = NumberAdder.add_numbers(3, 5)
    print(result)