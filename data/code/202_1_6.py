class LargestFinder:
    def __init__(self):
        self.largest = None

    def add_number(self, number):
        if self.largest is None or number > self.largest:
            self.largest = number

if __name__ == '__main__':
    finder = LargestFinder()
    for num in (3.14, 2.71, 1.618):
        finder.add_number(num)
    print(finder.largest)