class QuickAccessList:
    def __init__(self, elements):
        if not isinstance(elements, list):
            raise ValueError("Input must be a list")
        self.first_element = elements[0] if elements else None

    def get_first(self):
        return self.first_element

    def has_elements(self):
        return self.first_element is not None

if __name__ == '__main__':
    sample_list = [7, 14, 21, 28]
    access_list = QuickAccessList(sample_list)
    print(access_list.get_first())
    print(access_list.has_elements())

    empty_list = []
    empty_access_list = QuickAccessList(empty_list)
    print(empty_access_list.get_first())
    print(empty_access_list.has_elements())