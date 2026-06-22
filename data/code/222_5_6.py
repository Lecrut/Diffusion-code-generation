class MinFinder:
    def __init__(self, lst):
        self.lst = iter(lst)

    def find_min(self):
        try:
            min_val = next(self.lst)
            for item in self.lst:
                if item < min_val:
                    min_val = item
            return min_val
        except StopIteration:
            return None

if __name__ == '__main__':
    sample_list = [34, 56, 23, 89, 12, 78]
    finder = MinFinder(sample_list)
    print(finder.find_min())