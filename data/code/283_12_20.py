class FirstDuplicateFinder:
    def __init__(self):
        self.seen = set()

    def find_first_duplicate(self, lst):
        for item in lst:
            if item in self.seen:
                return item
            self.seen.add(item)
        return None

if __name__ == '__main__':
    finder = FirstDuplicateFinder()
    sample_list = [10, 20, 30, 40, 50, 20, 60]
    print(finder.find_first_duplicate(sample_list))