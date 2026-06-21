class NumberProperties:
    def __init__(self, value):
        if not isinstance(value, (int, float)):
            raise ValueError("Input must be a numeric type")
        self.value = value

    def is_positive(self):
        return self.value > 0

    def is_even(self):
        return isinstance(self.value, int) and self.value % 2 == 0

    def is_divisible_by_three(self):
        return isinstance(self.value, int) and self.value % 3 == 0

    def get_properties(self):
        return {
            "value": self.value,
            "is_positive": self.is_positive(),
            "is_even": self.is_even(),
            "is_divisible_by_three": self.is_divisible_by_three()
        }

if __name__ == '__main__':
    test_values = [10, 15, -4, 6, 9.5]
    for val in test_values:
        try:
            num_props = NumberProperties(val)
            result = num_props.get_properties()
            print(result)
        except ValueError as e:
            print(f"Error for {val}: {e}")