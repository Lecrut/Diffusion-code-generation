class NumberAdder:
    def __init__(self):
        self.a = 5
        self.b = 3

    def sum_numbers(self):
        return self.a + self.b

if __name__ == '__main__':
    adder = NumberAdder()
    result = adder.sum_numbers()
    print(result)