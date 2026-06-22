class MinFinder:
    def find_min(self, numbers):
        return min(numbers)

if __name__ == '__main__':
    finder = MinFinder()
    sample_values = [15, 27, -3, 89, 0]
    print(finder.find_min(sample_values))