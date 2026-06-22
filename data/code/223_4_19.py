class MaxFinder:
    @staticmethod
    def find_highest_value(numbers):
        if not numbers:
            raise ValueError("The list is empty")
        return max(numbers)

if __name__ == '__main__':
    sample_values = [15, 8, 3, 20, 7]
    try:
        print(MaxFinder.find_highest_value(sample_values))
    except ValueError as e:
        print(e)