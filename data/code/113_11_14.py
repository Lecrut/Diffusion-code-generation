class LargeIntSubtractor:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def subtract(self):
        return self.a - self.b

if __name__ == '__main__':
    subtractor = LargeIntSubtractor(12345678901234567890, 9876543210987654321)
    print(subtractor.subtract())