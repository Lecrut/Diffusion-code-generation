class MaxFinder:
    def __init__(self, lst):
        if not lst:
            raise ValueError("List is empty")
        self.max_elem = lst[0]
        for elem in lst[1:]:
            if elem > self.max_elem:
                self.max_elem = elem

    def get_max(self):
        return self.max_elem

if __name__ == '__main__':
    sample_list = [7, 2, 9, 5, 3, 8]
    finder = MaxFinder(sample_list)
    print(finder.get_max())