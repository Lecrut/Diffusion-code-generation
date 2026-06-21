class LargestValueFinder:
    @staticmethod
    def find_largest(numbers):
        largest = numbers[0]
        for number in numbers:
            if number > largest:
                largest = number
        return largest

if __name__ == '__main__':
    sample_values = (3.14, 2.71, 1.618)
    finder = LargestValueFinder()
    result = finder.find_largest(sample_values)
    print(result)