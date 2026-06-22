class ElementChecker:

    def __init__(self, elements):
        self.elements = elements

    def are_all_equal(self):
        if not self.elements:
            return True
        first_element = self.elements[0]
        for element in self.elements:
            if element != first_element:
                return False
        return True
if __name__ == '__main__':
    checker1 = ElementChecker([5, 5, 5, 5])
    print(checker1.are_all_equal())
    checker2 = ElementChecker([10, 10, 10, 11])
    print(checker2.are_all_equal())