class LargestNumberFinder:
    @staticmethod
    def find_largest(numbers):
        largest = numbers[0]
        for number in numbers:
            if number > largest:
                largest = number
        return largest

if __name__ == '__main__':
    sample_data = [3, 5, 1, 2, 4, 5, 9, 8, 7, 6, 9]
    print(LargestNumberFinder.find_largest(sample_data))