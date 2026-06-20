class NumberDifference:
    def __init__(self, value1=10, value2=5):
        self.value1 = value1
        self.value2 = value2

    def compute_difference(self):
        return abs(self.value1 - self.value2)

if __name__ == '__main__':
    diff_instance = NumberDifference()
    print(diff_instance.compute_difference())

    diff_instance2 = NumberDifference(3.5, 2.5)
    print(diff_instance2.compute_difference())