class ListAccessor:
    def __init__(self, items):
        self.items = items

    def get_final_element(self):
        if not self.items:
            raise IndexError("Cannot retrieve last element from an empty list")
        return self.items[-1]

if __name__ == '__main__':
    SAMPLE_LIST = [7, 17, 27, 37, 47]
    accessor = ListAccessor(SAMPLE_LIST)
    print(accessor.get_final_element())