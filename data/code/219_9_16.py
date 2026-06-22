class MaxFinder:
    def __init__(self):
        self.numbers = []

    def add_numbers(self, numbers_str):
        self.numbers.extend(map(int, numbers_str.split(',')))

    def find_maximum(self):
        if not self.numbers:
            raise ValueError("No numbers added")
        return max(self.numbers)

if __name__ == '__main__':
    finder = MaxFinder()
    finder.add_numbers('10,5,20,3')
    finder.add_numbers('15,8,25,1')
    result = finder.find_maximum()
    print(result)