class NumberAdder:
    def __init__(self, value1, value2):
        self.value1 = value1
        self.value2 = value2

    def _validate_input(self):
        try:
            self.num1 = float(self.value1)
            self.num2 = float(self.value2)
        except ValueError:
            raise ValueError("Error: Invalid input. Please enter numeric values.")

    def calculate_sum(self):
        self._validate_input()
        return self.num1 + self.num2

if __name__ == '__main__':
    adder1 = NumberAdder(10, 5)
    print(f"10 + 5 = {adder1.calculate_sum()}")

    try:
        adder2 = NumberAdder("hello", 5)
        print(f"'hello' + 5 = {adder2.calculate_sum()}")
    except ValueError as e:
        print(e)

    adder3 = NumberAdder(3.5, 2.1)
    print(f"3.5 + 2.1 = {adder3.calculate_sum()}")

    try:
        adder4 = NumberAdder("a", "b")
        print(f"'a' + 'b' = {adder4.calculate_sum()}")
    except ValueError as e:
        print(e)