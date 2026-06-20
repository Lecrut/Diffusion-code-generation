class ElementComparator:
    DEFAULT_VALUE = "Index out of bounds"

    @staticmethod
    def get_element_from_list(lst, index):
        try:
            return lst[index]
        except IndexError:
            return ElementComparator.DEFAULT_VALUE

    @classmethod
    def compare_elements(cls, list1, list2, index):
        element1 = cls.get_element_from_list(list1, index)
        element2 = cls.get_element_from_list(list2, index)
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