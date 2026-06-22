class ValueSorter:
    def __init__(self, x, y, z):
        if not all(isinstance(i, (int, float)) for i in [x, y, z]):
            raise ValueError("All inputs must be numbers")
        self.values = sorted([x, y, z])

    def get_values(self):
        return self.values

if __name__ == '__main__':
    sorter = ValueSorter(5.1, 2, 8)
    print(sorter.get_values())