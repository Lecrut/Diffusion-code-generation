class MaxIndexFinder:
    def find_max_index(self, numbers):
        return max(enumerate(numbers), key=lambda x: x[1])[0]

if __name__ == '__main__':
    finder = MaxIndexFinder()
    sample_numbers = [34, 78, 23, 65, 98]
    result = finder.find_max_index(sample_numbers)
    print(result)