class AscendingValues:
    def __init__(self, a, b, c):
        self.values = sorted([a, b, c])

    def get_values(self):
        return self.values

if __name__ == '__main__':
    values = AscendingValues(7, 4, 1)
    print(values.get_values())