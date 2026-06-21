class MaxFinder:
    @staticmethod
    def find_max(numbers):
        if not numbers:
            return None
        max_num = numbers[0]
        for num in numbers:
            if num > max_num:
                max_num = num
        return max_num

if __name__ == '__main__':
    sample_values = [3, 5, 1, 8, 2, 9, 4]
    max_value = MaxFinder.find_max(sample_values)
    print(max_value)