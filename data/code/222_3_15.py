class MinFinder:
    def __init__(self, lst):
        self.lst = lst

    def find_min(self):
        return min(self.lst)

if __name__ == '__main__':
    sample_list = [3, 5, 1, 2, 4]
    finder = MinFinder(sample_list)
    print(finder.find_min())