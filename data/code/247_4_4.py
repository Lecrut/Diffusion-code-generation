class LargeIntegerSum:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def compute_sum(self):
        return self.a + self.b

if __name__ == '__main__':
    instance = LargeIntegerSum(12345678901234567890, 98765432109876543210)
    result = instance.compute_sum()
    print(result)