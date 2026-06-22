class SortedValues:
    def __init__(self, x, y, z):
        self.a = min(x, y, z)
        self.c = max(x, y, z)
        self.b = x + y + z - self.a - self.c

    def get_values(self):
        return [self.a, self.b, self.c]

if __name__ == '__main__':
    values = SortedValues(5, 2, 8)
    print(values.get_values())