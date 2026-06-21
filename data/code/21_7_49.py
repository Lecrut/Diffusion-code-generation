class Sorter:
    def __init__(self, numbers):
        self.numbers = numbers

    def sort_by_descending(self):
        return sorted(self.numbers, reverse=True)

if __name__ == '__main__':
    sample_values = [7, 2, 5, 3, 8, 6]
    sorter_instance = Sorter(sample_values)
    sorted_values = sorter_instance.sort_by_descending()
    print(sorted_values)