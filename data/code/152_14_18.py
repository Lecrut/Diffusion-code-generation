class SharedElementsFinder:
    def __init__(self, list1, list2):
        self.set1 = set(list1)
        self.list2 = list2

    def find_common_elements(self):
        return [item for item in self.list2 if item in self.set1]

if __name__ == '__main__':
    finder = SharedElementsFinder([1, 2, 3, 4], [3, 4, 5, 6])
    common = finder.find_common_elements()
    print(common)