class LargeInteger:
    def __init__(self, value):
        self.value = value

    def subtract(self, other):
        return LargeInteger(self.value - other.value)

if __name__ == '__main__':
    a = LargeInteger(12345678901234567890)
    b = LargeInteger(98765432109876543210)
    result = a.subtract(b)
    print(result.value)