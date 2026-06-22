class ListAccessor:
    def __init__(self, elements):
        self.elements = elements

    def get_second(self):
        if len(self.elements) < 2:
            return None
        return self.elements[1]

if __name__ == '__main__':
    sample_lists = {
        'list1': [10, 20, 30, 40],
        'list2': [5],
        'list3': [],
        'list4': [1]
    }

    for name, lst in sample_lists.items():
        accessor = ListAccessor(lst)
        print(f"{name}: {accessor.get_second()}")