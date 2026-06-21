class MinFinder:
    EMPTY_LIST_ERROR = "Input list cannot be empty"

    @staticmethod
    def find_minimum(data):
        if not data:
            raise ValueError(MinFinder.EMPTY_LIST_ERROR)
        minimum = data[0]
        for number in data[1:]:
            if number < minimum:
                minimum = number
        return minimum

if __name__ == '__main__':
    sample_list = [3.14, 1.618, 2.718, -0.5, 9.99]
    min_finder = MinFinder()
    result = min_finder.find_minimum(sample_list)
    print(result)