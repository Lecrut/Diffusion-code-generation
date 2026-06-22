class NumberAdder:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def add_numbers(self):
        return self.num1 + self.num2

if __name__ == '__main__':
    adder_instance = NumberAdder(3.5, 2.5)
    result = adder_instance.add_numbers()
    print(result)