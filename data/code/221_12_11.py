class NumericSorter:
    def __init__(self, x, y, z):
        self.numbers = [x, y, z]
    
    def sort_values(self):
        return sorted(self.numbers)

if __name__ == '__main__':
    sorter = NumericSorter(7, 3, 5)
    sorted_list = sorter.sort_values()
    print(sorted_list)