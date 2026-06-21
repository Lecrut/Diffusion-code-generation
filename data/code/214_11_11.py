class MinFinder:
    def __init__(self, data):
        self.data = data

    def find_minimum(self):
        if not self.data:
            raise ValueError("Input iterable cannot be empty")
        minimum = self.data[0]
        for item in self.data[1:]:
            if item < minimum:
                minimum = item
        return minimum

if __name__ == '__main__':
    sample_list = [3, 1, 4, 1, 5, 9, 2, 8]
    min_finder_list = MinFinder(sample_list)
    result_list = min_finder_list.find_minimum()
    print(result_list)

    sample_tuple = (5, 12, 3, 8, 1, 9)
    min_finder_tuple = MinFinder(list(sample_tuple))
    result_tuple = min_finder_tuple.find_minimum()
    print(result_tuple)

    sample_single = [100]
    min_finder_single = MinFinder(sample_single)
    result_single = min_finder_single.find_minimum()
    print(result_single)