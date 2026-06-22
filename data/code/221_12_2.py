class AscendingValues:
    def __init__(self, values):
        self.values = sorted(values)

    def get_values(self):
        return self.values

if __name__ == '__main__':
    values = AscendingValues([5, 2, 8])
    print(values.get_values())