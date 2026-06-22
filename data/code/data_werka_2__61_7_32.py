class ListAccessor:
    def __init__(self, lst):
        self.lst = lst

    def validate_index(self, index):
        if not isinstance(index, int):
            raise ValueError("Index must be an integer")
        if index < 0 or index >= len(self.lst):
            raise IndexError("Index out of bounds")

    def get_element_at_index(self, index):
        self.validate_index(index)
        return self.lst[index]

if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5]
    accessor = ListAccessor(sample_list)
    try:
        index_to_find = 2
        element = accessor.get_element_at_index(index_to_find)
        print(element)
    except (ValueError, IndexError) as e:
        print(e)

    try:
        invalid_index = -1
        element = accessor.get_element_at_index(invalid_index)
        print(element)
    except (ValueError, IndexError) as e:
        print(e)