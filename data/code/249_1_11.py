class LargestItemFinder:
    @staticmethod
    def find_largest(numbers):
        if not numbers:
            raise ValueError("Input list cannot be empty")
        largest = numbers[0]
        for number in numbers[1:]:
            if number > largest:
                largest = number
        return largest

if __name__ == '__main__':
    sample_values = [3.14, 2.71, 1.618, 0.577, 1.414]
    finder = LargestItemFinder()
    result = finder.find_largest(sample_values)
    print(result)