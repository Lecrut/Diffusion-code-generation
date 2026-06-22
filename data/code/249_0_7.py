class MaxFinder:
    @staticmethod
    def find_largest(numbers):
        return max(numbers) if numbers else None

if __name__ == '__main__':
    sample_values = [3, 5, 1, 2, 4]
    print(MaxFinder.find_largest(sample_values))
    empty_list = []
    print(MaxFinder.find_largest(empty_list))