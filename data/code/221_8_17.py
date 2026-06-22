class NumberSorter:
    def __init__(self):
        self.numbers = [34, 7, 23]

    def sort_numbers(self):
        return sorted(self.numbers)

if __name__ == '__main__':
    sorter = NumberSorter()
    sorted_nums = sorter.sort_numbers()
    print(sorted_nums)