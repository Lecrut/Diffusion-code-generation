class MaxFinder:
    @classmethod
    def find_largest(cls, numbers):
        return max(numbers)

if __name__ == '__main__':
    sample_numbers = [3, 5, 1, 2, 4]
    print(MaxFinder.find_largest(sample_numbers))