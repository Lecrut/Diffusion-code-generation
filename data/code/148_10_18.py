class MaxFinder:
    def find_largest(self, numbers):
        if not numbers:
            return None
        largest = numbers[0]
        for number in numbers:
            if number > largest:
                largest = number
        return largest

if __name__ == '__main__':
    finder = MaxFinder()
    sample_list = [10, 5, 20, 8, 15]
    largest = finder.find_largest(sample_list)
    print(largest)