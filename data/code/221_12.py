class NumberSorter:
    def __init__(self, a, b, c):
        self.numbers = [a, b, c]
    def sort_numbers(self):
        self.numbers.sort()
        return self.numbers
if __name__ == '__main__':
    sorter = NumberSorter(5, 2, 8)
    sorted_list = sorter.sort_numbers()
    print(sorted_list)