class NumberAdder:
    def __init__(self, value1, value2):
        self.value1 = value1
        self.value2 = value2

    def calculate_sum(self):
        try:
            num1 = float(self.value1)
            num2 = float(self.value2)
            return num1 + num2
        except ValueError:
            return "Error: Invalid input. Please enter numeric values."

if __name__ == '__main__':
    adder1 = NumberAdder(10, 5)
    print(f"Sum of 10 and 5 is {adder1.calculate_sum()}")

    adder2 = NumberAdder("hello", 5)
    print(f"Sum of 'hello' and 5 is {adder2.calculate_sum()}")

    adder3 = NumberAdder(3.5, 2.1)
    print(f"Sum of 3.5 and 2.1 is {adder3.calculate_sum()}")

    adder4 = NumberAdder("a", "b")
    print(f"Sum of 'a' and 'b' is {adder4.calculate_sum()}")