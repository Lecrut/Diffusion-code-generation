class MaxFinder:
    @staticmethod
    def find_maximum(numbers):
        if not numbers:
            raise ValueError("Input list cannot be empty")
        max_value = numbers[0]
        for number in numbers:
            if number > max_value:
                max_value = number
        return max_value

if __name__ == '__main__':
    sample_list = [3.14, 1.618, 2.718, 0.577, 9.99]
    try:
        max_value = MaxFinder.find_maximum(sample_list)
        print(max_value)
    except ValueError as e:
        print(e)