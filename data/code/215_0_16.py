class NumberFinder:
    @staticmethod
    def find_largest_number(numbers):
        if not numbers:
            return None
        return max(numbers)

if __name__ == '__main__':
    sample_data = [10, 5, 20, 3, 15]
    largest_number = NumberFinder.find_largest_number(sample_data)
    print(largest_number)