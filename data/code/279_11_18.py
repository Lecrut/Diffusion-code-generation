class ReverseIterator:
    def __init__(self, numbers):
        self.numbers = numbers
        self.index = len(numbers) - 1

    @staticmethod
    def create(sample_values):
        return ReverseIterator(sample_values)

    def next(self):
        if self.index >= 0:
            value = self.numbers[self.index]
            self.index -= 1
            return value
        else:
            raise StopIteration

if __name__ == '__main__':
    sample_values = [1, 2, 3, 4, 5]
    reverse_iterator = ReverseIterator.create(sample_values)
    while True:
        try:
            print(reverse_iterator.next())
        except StopIteration:
            break