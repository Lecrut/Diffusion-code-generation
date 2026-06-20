class FloatDifference:
    def __init__(self, value1, value2):
        self.value1 = value1
        self.value2 = value2

    def compute_difference(self):
        return self.value1 - self.value2

if __name__ == '__main__':
    diff_instance = FloatDifference(10.5, 4.2)
    result = diff_instance.compute_difference()
    print(result)