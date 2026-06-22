class ElementEqualityChecker:

    def __init__(self, elements):
        self.elements = elements

    def are_all_elements_equal(self):
        if not self.elements:
            return True
        first_element = self.elements[0]
        for element in self.elements:
            if element != first_element:
                return False
        return True
if __name__ == '__main__':
    checker1 = ElementEqualityChecker([42, 42, 42])
    print(checker1.are_all_elements_equal())
    checker2 = ElementEqualityChecker([17, 17, 17, 17])
    print(checker2.are_all_elements_equal())
    checker3 = ElementEqualityChecker([1, 2, 3])
    print(checker3.are_all_elements_equal())