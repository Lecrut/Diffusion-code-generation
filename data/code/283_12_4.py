class DuplicateFinder:
    def __init__(self):
        self.seen = set()

    def find_first_duplicate(self, lst):
        for item in lst:
            if item in self.seen:
                return item
            self.seen.add(item)
        return None

if __name__ == '__main__':
    finder = DuplicateFinder()
    sample_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 2]
    print(finder.find_first_duplicate(sample_list))