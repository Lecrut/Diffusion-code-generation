class MinStringFinder:
    @staticmethod
    def get_minimum(data):
        if not data:
            raise ValueError("Input list cannot be empty")
        minimum = data[0]
        for item in data[1:]:
            if item < minimum:
                minimum = item
        return minimum

if __name__ == '__main__':
    sample_list = ['banana', 'apple', 'cherry']
    min_finder = MinStringFinder()
    minimum_value = min_finder.get_minimum(sample_list)
    print(minimum_value)