class MaxFinder:
    def find_max(self, iterable):
        return max(iterable)
if __name__ == '__main__':
    finder = MaxFinder()
    sample_data = [10, 50, 23, 87, 4]
    result = finder.find_max(sample_data)
    print(result)