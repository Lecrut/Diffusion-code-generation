class SumCalculator:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def calculate_sum(self):
        return self.a + self.b

if __name__ == '__main__':
    instance = SumCalculator(10, 20)
    print(instance.calculate_sum())