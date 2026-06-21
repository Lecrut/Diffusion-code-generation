from functools import reduce

class MinFinder:
    MIN_VALUE = float('inf')

    @staticmethod
    def find_minimum(data):
        if not data:
            raise ValueError("Input list cannot be empty")
        return reduce(lambda x, y: x if x < y else y, data, MinFinder.MIN_VALUE)

if __name__ == '__main__':
    large_list = [random.randint(0, 1000000) for _ in range(1000000)]
    min_finder = MinFinder()
    print(f"Minimum element found: {min_finder.find_minimum(large_list)}")