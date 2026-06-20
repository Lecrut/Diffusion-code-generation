class ValueSubtractor:
    def __init__(self, value):
        self.value = value

    def subtract(self, other):
        return ValueSubtractor(self.value - other.value)

if __name__ == '__main__':
    v1 = ValueSubtractor(10)
    v2 = ValueSubtractor(5)
    v3 = v1.subtract(v2)
    print(f"v1: {v1.value}")
    print(f"v2: {v2.value}")
    print(f"v3 (v1 - v2): {v3.value}")