class CommonElementsFinder:
    def __init__(self, list1, list2):
        self.set2 = set(list2)

    def find_common_elements(self):
        return [element for element in self.list1 if element in self.set2]

if __name__ == '__main__':
    finder = CommonElementsFinder([1, 2, 3, 4, 5], [4, 5, 6, 7, 8])
    print(finder.find_common_elements())