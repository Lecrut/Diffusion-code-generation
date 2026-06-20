class NumberDifference:
    def __init__(self, value1, value2):
        self.value1 = value1
        self.value2 = value2

    def compute_difference(self):
        return abs(self.value1 - self.value2)

if __name__ == '__main__':
    diff_instance = NumberDifference(10, 5)
    print(diff_instance.compute_difference())