class MaxFinder:
    @staticmethod
    def find_max(numbers):
        if not numbers:
            return None
        max_value = numbers[0]
        for num in numbers:
            if num > max_value:
                max_value = num
        return max_value

if __name__ == '__main__':
    sample_values = [10, 5, 22, 8, 30, 1]
    result = MaxFinder.find_max(sample_values)
    print(result)