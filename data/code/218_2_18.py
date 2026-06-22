class MinFinder:
    MIN_NOT_FOUND = float('inf')

    @staticmethod
    def find_minimum(data):
        if not data:
            return MinFinder.MIN_NOT_FOUND
        minimum = data[0]
        for number in data[1:]:
            if number < minimum:
                minimum = number
        return minimum

if __name__ == '__main__':
    sample_list = [3.14, 1.618, 2.718, -0.5, 9.99]
    finder = MinFinder()
    minimum_value = finder.find_minimum(sample_list)
    print(minimum_value)