class MinValueFinder:
    @staticmethod
    def find_min_value(data):
        return min(data)

if __name__ == '__main__':
    sample_data = [5, 3, 9, 1, 10]
    finder = MinValueFinder()
    smallest = finder.find_min_value(sample_data)
    print(smallest)