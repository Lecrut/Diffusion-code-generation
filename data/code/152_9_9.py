class ElementFinder:
    def __init__(self, list1, list2):
        self.set1 = set(list1)
        self.set2 = set(list2)

    def find_shared_elements(self):
        return self.set1.intersection(self.set2)

if __name__ == '__main__':
    finder = ElementFinder([1, 2, 3, 4, 5], [4, 5, 6, 7, 8])
    shared_elements = finder.find_shared_elements()
    print(shared_elements)