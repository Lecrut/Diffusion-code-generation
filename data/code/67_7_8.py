class NumberAdder:
    def __init__(self, value1, value2):
        self.value1 = value1
        self.value2 = value2

    def _validate_and_convert(self, value):
        try:
            return float(value)
        except ValueError:
            raise ValueError(f"Invalid input: {value} is not a numeric value.")

    def calculate_sum(self):
        num1 = self._validate_and_convert(self.value1)
        num2 = self._validate_and_convert(self.value2)
        return num1 + num2

if __name__ == '__main__':
    adder1 = NumberAdder(10, 5)
    print(f"Sum of 10 and 5: {adder1.calculate_sum()}")

    adder2 = NumberAdder("3.5", "2.1")
    print(f"Sum of '3.5' and '2.1': {adder2.calculate_sum()}")

    try:
        adder3 = NumberAdder("hello", 5)
        print(f"Sum of 'hello' and 5: {adder3.calculate_sum()}")
    except ValueError as e:
        print(e)

    try:
        adder4 = NumberAdder("a", "b")
        print(f"Sum of 'a' and 'b': {adder4.calculate_sum()}")
    except ValueError as e:
        print(e)