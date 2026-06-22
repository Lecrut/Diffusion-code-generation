class MaxFinder:
    def find_largest(self, data):
        return max(data) if data else None

if __name__ == '__main__':
    finder = MaxFinder()
    sample_values = [3, 5, 1, 2, 4]
    print(finder.find_largest(sample_values))
    empty_list = []
    print(finder.find_largest(empty_list))