class NumberAdder:
    def add_numbers(self, a, b):
        return a + b

if __name__ == '__main__':
    adder = NumberAdder()
    result1 = adder.add_numbers(3, 5)
    result2 = adder.add_numbers(7, 9)
    print(result1)
    print(result2)