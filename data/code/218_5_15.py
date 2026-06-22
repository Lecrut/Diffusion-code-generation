class MinFinder:
    @staticmethod
    def find_min(numbers):
        return min(numbers)

if __name__ == '__main__':
    sample_data = [10, 5, 20, 3, 15]
    minimum_value = MinFinder.find_min(sample_data)
    print(minimum_value)