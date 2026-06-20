class ValueDifference:
    def __init__(self, value1=3.5, value2=2.1):
        self.value1 = value1
        self.value2 = value2

    def compute_difference(self):
        return self.value1 - self.value2

if __name__ == '__main__':
    diff_instance = ValueDifference()
    result = diff_instance.compute_difference()
    print(result)