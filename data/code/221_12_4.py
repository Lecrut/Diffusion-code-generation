class AscendingValues:
    def __init__(self, a, b, c):
        self.values = sorted([a, b, c])

    def get_values(self):
        return self.values

if __name__ == '__main__':
    av = AscendingValues(3, 1, 2)
    print(av.get_values())