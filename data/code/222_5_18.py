class MinFinder:
    MIN_VALUE = float('inf')

    @staticmethod
    def find_min(lst):
        min_val = MinFinder.MIN_VALUE
        for item in lst:
            if item < min_val:
                min_val = item
        return min_val

if __name__ == '__main__':
    sample_list = [34, 56, 23, 89, 12, 78]
    minimum = MinFinder.find_min(sample_list)
    print(minimum)