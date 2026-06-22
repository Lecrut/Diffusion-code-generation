class AscendingValues:
    def __init__(self, a, b, c):
        self.values = [a, b, c]
        self.sort_values()

    def sort_values(self):
        for i in range(len(self.values)):
            for j in range(i + 1, len(self.values)):
                if self.values[i] > self.values[j]:
                    self.values[i], self.values[j] = self.values[j], self.values[i]

if __name__ == '__main__':
    values = AscendingValues(3, 1, 2)
    print(values.values)