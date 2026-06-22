class MaxFinder:
    @staticmethod
    def find_maximum(numbers):
        if not numbers:
            return None
        max_value = numbers[0]
        for row in numbers:
            for number in row:
                if number > max_value:
                    max_value = number
        return max_value

if __name__ == '__main__':
    input_data = [
        [10, 5, 20],
        [8, 15],
        [3, 9, 42, 1]
    ]
    result = MaxFinder.find_maximum(input_data)
    print(result)