class NumberDifference:
    def __init__(self, value1=10, value2=5):
        self.value1 = value1
        self.value2 = value2

    @staticmethod
    def calculate_difference(value1, value2):
        return abs(value1 - value2)

if __name__ == '__main__':
    diff_instance = NumberDifference()
    print(diff_instance.calculate_difference(10, 5))