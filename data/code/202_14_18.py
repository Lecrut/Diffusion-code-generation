class LargestNumberFinder:
    def __init__(self, numbers):
        self.numbers = numbers
    
    def find_largest_number(self):
        return max(self.numbers)

if __name__ == '__main__':
    sample_values = [15, 27, 39, 42, 6]
    finder = LargestNumberFinder(sample_values)
    print(finder.find_largest_number())