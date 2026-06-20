class NumberDifference:
    def __init__(self, value1, value2):
        self.value1 = value1
        self.value2 = value2

    def compute_difference(self):
        return abs(self.value1 - self.value2)

if __name__ == '__main__':
    sample_value1 = 10
    sample_value2 = 5
    diff_instance = NumberDifference(sample_value1, sample_value2)
    print(diff_instance.compute_difference())