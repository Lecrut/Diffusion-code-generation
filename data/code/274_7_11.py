class CommonElementsFinder:
    def __init__(self, list1, list2):
        self.list1 = list1
        self.list2 = list2
    
    def find_commons(self):
        common_elements = [element for element in self.list1 if element in self.list2]
        return common_elements

if __name__ == '__main__':
    sample_list1 = [1, 2, 3, 4, 5]
    sample_list2 = [4, 5, 6, 7, 8]
    
    finder = CommonElementsFinder(sample_list1, sample_list2)
    common_elements = finder.find_commons()
    print(common_elements)