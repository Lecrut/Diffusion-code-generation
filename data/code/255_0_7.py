class MaxFinder:
    @staticmethod
    def find_maximum(numbers):
        if not numbers:
            return None
        max_element = numbers[0]
        for number in numbers[1:]:
            if number > max_element:
                max_element = number
        return max_element

if __name__ == '__main__':
    sample_list = [10, 5, 20, 8, 15]
    result = MaxFinder.find_maximum(sample_list)
    print(result)