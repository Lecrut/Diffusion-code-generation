class MaxFinder:
    @staticmethod
    def find_max(numbers):
        return max(numbers)

if __name__ == '__main__':
    sample_data = [10, 5, 22, 8, 30, 15]
    largest_number = MaxFinder.find_max(sample_data)
    print(largest_number)