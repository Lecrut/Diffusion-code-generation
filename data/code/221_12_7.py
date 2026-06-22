class SortedNumbers:
    def __init__(self, x, y, z):
        self.numbers = sorted([x, y, z])
    
    def get_numbers(self):
        return self.numbers

if __name__ == '__main__':
    sorter = SortedNumbers(7, 1, 4)
    sorted_list = sorter.get_numbers()
    print(sorted_list)