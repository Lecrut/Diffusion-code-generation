class AscendingValues:
    def __init__(self, a, b, c):
        self.values = sorted([a, b, c])

    def get_values(self):
        return self.values

if __name__ == '__main__':
    values = AscendingValues(3, 1, 2)
    print(values.get_values())