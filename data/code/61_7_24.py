class SafeListAccess:
    def __init__(self, lst):
        self.lst = lst

    def get_element_at_index(self, index):
        if not isinstance(index, int):
            raise ValueError("Index must be an integer")
        if index < 0 or index >= len(self.lst):
            raise IndexError("Index out of bounds")
        return self.lst[index]

if __name__ == '__main__':
    sample_list = [5, 15, 25, 35, 45]
    index_to_find = 1
    safe_access = SafeListAccess(sample_list)
    try:
        element = safe_access.get_element_at_index(index_to_find)
        print(element)
    except (ValueError, IndexError) as e:
        print(e)