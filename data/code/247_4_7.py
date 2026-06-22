class LargeIntegerSum:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def compute_sum(self):
        return self.a + self.b

if __name__ == '__main__':
    instance1 = LargeIntegerSum(12345678901234567890, 98765432109876543210)
    result1 = instance1.compute_sum()
    print(result1)

    instance2 = LargeIntegerSum(98765432109876543210, 12345678901234567890)
    result2 = instance2.compute_sum()
    print(result2)