class MinItemFinder:
    @staticmethod
    def find_min_item(items):
        return min((item for item in items), default=None)

if __name__ == '__main__':
    sample_items = [5, 3, 9, 1, 4]
    finder = MinItemFinder()
    print(finder.find_min_item(sample_items))