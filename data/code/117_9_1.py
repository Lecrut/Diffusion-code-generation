class NumberDifference:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def compute_difference(self):
        return abs(self.a - self.b)

if __name__ == '__main__':
    diff_instance = NumberDifference(10, 5)
    print(diff_instance.compute_difference())