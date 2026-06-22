class NumberSorter:
    def __init__(self, x, y, z):
        self.values = [x, y, z]

    def sort_numbers(self):
        return sorted(self.values)

if __name__ == '__main__':
    sorter = NumberSorter(5, 2, 8)
    print(sorter.sort_numbers())