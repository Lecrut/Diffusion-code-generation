class LargestValueFinder:
    def __init__(self, numbers):
        self.numbers = numbers

    def find_largest(self):
        largest = self.numbers[0]
        for number in self.numbers:
            if number > largest:
                largest = number
        return largest

if __name__ == '__main__':
    finder1 = LargestValueFinder([10, 5, 20, 8])
    print(finder1.find_largest())

    finder2 = LargestValueFinder([-5, -1, -10, -3])
    print(finder2.find_largest())

    finder3 = LargestValueFinder([42])
    print(finder3.find_largest())

    finder4 = LargestValueFinder([7])
    print(finder4.find_largest())