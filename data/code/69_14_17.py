class ListAccessor:

    def __init__(self, elements):
        self.elements = elements

    def get_first_element(self):
        if not self.elements:
            return None
        return self.elements[0]

    def get_last_element(self):
        if not self.elements:
            return None
        return self.elements[-1]

    def get_middle_element(self):
        if not self.elements:
            return None
        mid_index = len(self.elements) // 2
        return self.elements[mid_index]

def access_elements(elements):
    accessor = ListAccessor(elements)
    first = accessor.get_first_element()
    last = accessor.get_last_element()
    middle = accessor.get_middle_element()
    return (first, last, middle)
if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    result = access_elements(sample_list)
    print(result)
    empty_list = []
    result_empty = access_elements(empty_list)
    print(result_empty)