class LargestElementFinder:
    def find_largest(self, numbers):
        largest = numbers[0]
        for number in numbers:
            if number > largest:
                largest = number
        return largest

if __name__ == '__main__':
    finder = LargestElementFinder()
    sample_data = [10, 5, 20, 15, 30]
    print(finder.find_largest(sample_data))