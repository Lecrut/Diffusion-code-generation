class Sorter:
    def __init__(self, numbers):
        self.numbers = numbers

    def sort_by_descending(self):
        return sorted(self.numbers, reverse=True)

if __name__ == '__main__':
    sample_values = [7, 2, 9, 4, 6]
    sorter_instance = Sorter(sample_values)
    sorted_values = sorter_instance.sort_by_descending()
    print(sorted_values)

    another_sample = [15, 3, -10, 8, 0]
    another_sorter = Sorter(another_sample)
    another_sorted = another_sorter.sort_by_descending()
    print(another_sorted)