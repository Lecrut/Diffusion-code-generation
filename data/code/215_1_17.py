class MaxFinder:
    def __init__(self, numbers):
        self.numbers = numbers

    def find_largest(self):
        largest = self.numbers[0]
        for number in self.numbers:
            if number > largest:
                largest = number
        return largest

if __name__ == '__main__':
    finder1 = MaxFinder((99, 45, 67, 12, 88))
    result1 = finder1.find_largest()
    print(result1)