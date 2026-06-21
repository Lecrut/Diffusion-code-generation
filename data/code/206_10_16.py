class NumberUtils:
    @staticmethod
    def find_minimum(numbers):
        return min(numbers)

if __name__ == '__main__':
    sample_values = [4, 2, 9, 7, 5]
    result = NumberUtils.find_minimum(sample_values)
    print(result)