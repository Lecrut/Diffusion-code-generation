class NumberAdder:
    def __init__(self):
        self.result = 0

    def add(self, a, b):
        try:
            num1 = float(a)
            num2 = float(b)
            self.result = num1 + num2
            return self.result
        except ValueError:
            return "Error: Invalid input. Please enter numeric values."

if __name__ == '__main__':
    adder = NumberAdder()
    print(adder.add(10, 5))
    print(adder.add("20", 3.5))
    print(adder.add(7, "eight"))
    print(adder.add(-5, -10))
    print(adder.add("a", "b"))