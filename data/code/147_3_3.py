class NumberSorter:
    def __init__(self, numbers):
        self.numbers = numbers

    def sort_descending(self):
        return sorted(self.numbers, reverse=True)

if __name__ == '__main__':
    sorter = NumberSorter([3.5, 1.2, 4.8, 2.9])
    sorted_numbers = sorter.sort_descending()
    print(sorted_numbers)