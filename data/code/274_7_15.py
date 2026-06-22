class CommonElementsFinder:
    def __init__(self, list1, list2):
        self.list1 = list1
        self.list2 = list2

    def find_common_elements(self):
        common = [element for element in self.list1 if element in self.list2]
        return common

if __name__ == '__main__':
    finder = CommonElementsFinder([1, 2, 3, 4, 5], [4, 5, 6, 7, 8])
    print(finder.find_common_elements())