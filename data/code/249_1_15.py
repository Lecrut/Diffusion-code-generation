class ListProcessor:
    def __init__(self, numbers):
        self.numbers = numbers

    def find_largest(self):
        if not self.numbers:
            raise ValueError("Input list cannot be empty")
        largest = self.numbers[0]
        for number in self.numbers[1:]:
            if number > largest:
                largest = number
        return largest

if __name__ == '__main__':
    sample_list = [15.7, 8.2, 22.3, 4.9, 30.1, 11.6]
    processor = ListProcessor(sample_list)
    result = processor.find_largest()
    print(result)