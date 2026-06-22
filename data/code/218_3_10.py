class MinStringFinder:
    @staticmethod
    def find_minimum(data):
        if not data:
            raise ValueError("Input list cannot be empty")
        return min(data)

if __name__ == '__main__':
    sample_list = ['banana', 'apple', 'cherry']
    minimum_value = MinStringFinder.find_minimum(sample_list)
    print(minimum_value)