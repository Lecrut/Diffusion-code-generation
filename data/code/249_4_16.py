class MaxFinder:
    def find_largest(self, numbers):
        if not numbers:
            raise ValueError("The list is empty")
        return max(numbers)

if __name__ == '__main__':
    sample_list = [10, 5, 42, 3, 99, 21]
    finder = MaxFinder()
    largest_value = finder.find_largest(sample_list)
    print(largest_value)