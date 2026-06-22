class MinMaxFinder:
    MIN_VALUE = float('inf')
    MAX_VALUE = float('-inf')

    @staticmethod
    def find_min_max(numbers):
        if not numbers:
            raise ValueError("The list is empty")

        minimum = MinMaxFinder.MIN_VALUE
        maximum = MinMaxFinder.MAX_VALUE

        for number in numbers:
            if number < minimum:
                minimum = number
            elif number > maximum:
                maximum = number

        return minimum, maximum

if __name__ == '__main__':
    data = [15, 3, 88, 42, 9, 76]
    min_val, max_val = MinMaxFinder.find_min_max(data)
    print(f"Minimum value: {min_val}")
    print(f"Maximum value: {max_val}")