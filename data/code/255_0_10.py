class MaxFinder:
    NO_ELEMENT = None

    @staticmethod
    def find_maximum(numbers):
        if not numbers:
            return MaxFinder.NO_ELEMENT
        max_element = numbers[0]
        for number in numbers[1:]:
            if number > max_element:
                max_element = number
        return max_element

if __name__ == '__main__':
    sample_values = [7, 3, 9, 2, 5, 1, 8]
    result = MaxFinder.find_maximum(sample_values)
    print(result)