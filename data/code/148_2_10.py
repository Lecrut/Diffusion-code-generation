class LargestElementFinder:
    @staticmethod
    def find_largest_element(numbers):
        if not numbers:
            return None
        largest_value = numbers[0]
        for number in numbers:
            if number > largest_value:
                largest_value = number
        return largest_value

if __name__ == '__main__':
    sample_data = [10, 5, 20, 15, 30]
    result = LargestElementFinder.find_largest_element(sample_data)
    print(result)