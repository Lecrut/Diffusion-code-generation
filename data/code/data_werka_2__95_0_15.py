class NumberProperties:
    def __init__(self, value):
        self.value = value

    def is_positive(self):
        return self.value > 0

    def is_even(self):
        return self.value % 2 == 0

    def is_divisible_by_three(self):
        return self.value % 3 == 0

    def get_properties(self):
        return {
            "is_positive": self.is_positive(),
            "is_even": self.is_even(),
            "is_divisible_by_three": self.is_divisible_by_three()
        }

if __name__ == '__main__':
    test_values = [21, 8, -12, 0, 7]
    for val in test_values:
        obj = NumberProperties(val)
        props = obj.get_properties()
        print(f"Value: {val}, Properties: {props}")