class MaxFinder:
    @staticmethod
    def find_highest_value(numbers):
        if not numbers:
            raise ValueError("The list is empty")
        return max(numbers)

if __name__ == '__main__':
    sample_values = [12, 45, 78, 34, 90]
    try:
        print(MaxFinder.find_highest_value(sample_values))
    except ValueError as e:
        print(e)