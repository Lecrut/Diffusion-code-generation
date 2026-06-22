from functools import reduce

def find_max(numbers):
    return reduce(lambda x, y: x if x > y else y, numbers)

class MaxFinder:

    def __init__(self, numbers):
        self.numbers = numbers

    def get_numbers(self):
        return self.numbers

    def set_numbers(self, new_numbers):
        self.numbers = new_numbers

    def find_max(self):
        return reduce(lambda x, y: x if x > y else y, self.numbers)
if __name__ == '__main__':
    sample_numbers = [3, 5, 1, 2, 4]
    finder = MaxFinder(sample_numbers)
    print('Current numbers:', finder.get_numbers())
    print('Max number:', finder.find_max())
    finder.set_numbers([10, 7, 5, 8, 2])
    print('Updated numbers:', finder.get_numbers())
    print('New max number:', finder.find_max())