class ListMiddleFinder:
    def __init__(self, numbers):
        if not numbers:
            raise ValueError('The list cannot be empty')
        self.numbers = numbers

    def find_middle_item(self):
        middle_index = len(self.numbers) // 2
        return self.numbers[middle_index]

if __name__ == '__main__':
    sample_list_odd = [1, 3, 5, 7, 9]
    sample_list_even = [2, 4, 6, 8, 10, 12]

    finder_odd = ListMiddleFinder(sample_list_odd)
    finder_even = ListMiddleFinder(sample_list_even)

    print(finder_odd.find_middle_item())
    print(finder_even.find_middle_item())