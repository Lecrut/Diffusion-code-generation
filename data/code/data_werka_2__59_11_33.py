class ListMiddleFinder:
    def __init__(self, numbers):
        if not numbers:
            raise ValueError("The list is empty")
        self.numbers = numbers

    def find_middle_item(self):
        index = len(self.numbers) // 2
        return self.numbers[index]

if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    finder = ListMiddleFinder(sample_list)
    middle_item = finder.find_middle_item()
    print(middle_item)

    another_sample = [5, 15, 25, 35, 45, 55]
    another_finder = ListMiddleFinder(another_sample)
    another_middle_item = another_finder.find_middle_item()
    print(another_middle_item)