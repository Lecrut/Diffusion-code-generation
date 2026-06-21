class MaxFinder:
    def __init__(self, lst):
        self.lst = lst

    def find_max(self):
        max_elem = self.lst[0]
        for elem in self.lst:
            if elem > max_elem:
                max_elem = elem
        return max_elem

if __name__ == '__main__':
    sample_list = [3, 5, 1, 2, 4]
    finder = MaxFinder(sample_list)
    print(finder.find_max())