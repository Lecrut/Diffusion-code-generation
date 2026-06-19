class NumberSummer:
    def __init__(self, value1, value2):
        self.value1 = value1
        self.value2 = value2

    @staticmethod
    def _parse_value(value):
        try:
            return float(value)
        except ValueError:
            raise ValueError("Error: Invalid input. Please enter numeric values.")

    def calculate_sum(self):
        parsed_value1 = NumberSummer._parse_value(self.value1)
        parsed_value2 = NumberSummer._parse_value(self.value2)
        return parsed_value1 + parsed_value2

if __name__ == '__main__':
    sum_calculator1 = NumberSummer(10, 5)
    print(f"10 + 5 = {sum_calculator1.calculate_sum()}")

    try:
        sum_calculator2 = NumberSummer("hello", 5)
        print(f"'hello' + 5 = {sum_calculator2.calculate_sum()}")
    except ValueError as e:
        print(e)

    sum_calculator3 = NumberSummer(3.5, 2.1)
    print(f"3.5 + 2.1 = {sum_calculator3.calculate_sum()}")

    try:
        sum_calculator4 = NumberSummer("a", "b")
        print(f"'a' + 'b' = {sum_calculator4.calculate_sum()}")
    except ValueError as e:
        print(e)