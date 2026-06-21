class MinFinder:
    def find_min_item(self, items):
        return min((item for item in items))

if __name__ == '__main__':
    sample_items = [5, 3, 9, 1, 10]
    finder = MinFinder()
    print(finder.find_min_item(sample_items))