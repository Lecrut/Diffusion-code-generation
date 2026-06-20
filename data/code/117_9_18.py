MAX_VALUE = 100

class NumberDifference:
    def __init__(self, value_a, value_b):
        if not (isinstance(value_a, int) and isinstance(value_b, int)):
            raise ValueError("Both inputs must be integers.")
        self.value_a = value_a
        self.value_b = value_b

    def compute_difference(self):
        return abs(self.value_a - self.value_b)

if __name__ == '__main__':
    diff_instance = NumberDifference(10, 5)
    print(diff_instance.compute_difference())