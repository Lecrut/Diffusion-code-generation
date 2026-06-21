class ElementFinder:
    def __init__(self, list2):
        self.set2 = set(list2)

    def find_common(self, list1):
        return [element for element in list1 if element in self.set2]

if __name__ == '__main__':
    finder = ElementFinder([4, 5, 6, 7, 8])
    sample_list1 = [1, 2, 3, 4, 5]
    common_elements = finder.find_common(sample_list1)
    print(common_elements)