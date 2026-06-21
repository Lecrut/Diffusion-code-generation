class MaxFinder:
    MAX_VALUE = float('-inf')

    @staticmethod
    def find_max_element(numbers):
        return max(numbers, default=MaxFinder.MAX_VALUE)

if __name__ == '__main__':
    sample_values = [3, 5, 1, 8, 2]
    print(MaxFinder.find_max_element(sample_values))