class CommonElementsFinder:
    def __init__(self, list1, list2):
        self.set2 = set(list2)
    
    def find_common_elements(self):
        return [element for element in self.list1 if element in self.set2]

if __name__ == '__main__':
    sample_list1 = [1, 2, 3, 4, 5]
    sample_list2 = [4, 5, 6, 7, 8]
    finder = CommonElementsFinder(sample_list1, sample_list2)
    common_elements = finder.find_common_elements()
    print(common_elements)