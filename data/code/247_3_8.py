class NumberAdder:
    @staticmethod
    def add_numbers(a=3, b=7):
        return a + b

if __name__ == '__main__':
    result = NumberAdder.add_numbers()
    print(result)