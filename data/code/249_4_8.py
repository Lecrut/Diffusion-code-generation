class MaxFinder:
    @staticmethod
    def find_largest(numbers):
        if not numbers:
            raise ValueError("The list is empty")
        return max((num for num in numbers), default=None)

if __name__ == '__main__':
    sample_data = [10, 5, 30, 8, 20]
    largest_value = MaxFinder.find_largest(sample_data)
    print(largest_value)