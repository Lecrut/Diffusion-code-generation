class LargeIntegerSum:
    @staticmethod
    def add(a, b):
        return a + b

if __name__ == '__main__':
    result = LargeIntegerSum.add(12345678901234567890, 98765432109876543210)
    print(result)