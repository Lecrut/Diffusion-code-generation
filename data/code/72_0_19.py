class ElementComparator:
    DEFAULT_VALUE = "Index out of bounds"

    @staticmethod
    def get_element(list_, index):
        try:
            return list_[index]
        except IndexError:
            return ElementComparator.DEFAULT_VALUE

    @staticmethod
    def compare_elements(list1, list2, index):
        element1 = ElementComparator.get_element(list1, index)
        element2 = ElementComparator.get_element(list2, index)
        return element1, element2

if __name__ == '__main__':
    comparator = ElementComparator()
    list_a = [10, 20, 30, 40]
    list_b = [5, 15, 25, 35]
    index_to_check = 2
    result = comparator.compare_elements(list_a, list_b, index_to_check)
    print(f"List A: {list_a}")
    print(f"List B: {list_b}")
    print(f"Index: {index_to_check}")
    print(f"Result: {result}")