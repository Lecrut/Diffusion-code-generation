class MaxFinder:
    def __init__(self, sorted_list):
        self.sorted_list = sorted_list

    def find_max(self):
        return self.sorted_list[-1]

if __name__ == '__main__':
    finder = MaxFinder([1, 2, 3, 4, 5])
    print(finder.find_max())