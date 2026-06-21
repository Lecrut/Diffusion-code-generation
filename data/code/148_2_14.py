class LargestElementFinder:
    def __init__(self, data):
        self.data = data

    def find_largest(self):
        largest_value = self.data[0]
        for number in self.data:
            if number > largest_value:
                largest_value = number
        return largest_value

if __name__ == '__main__':
    finder = LargestElementFinder([10, 5, 20, 15, 30])
    print(finder.find_largest())