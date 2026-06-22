class ListAccessor:
    MAX_INDEX = 10000

    @staticmethod
    def is_valid_index(index):
        return isinstance(index, int) and 0 <= index < ListAccessor.MAX_INDEX

    def __init__(self, lst):
        self.lst = lst

    def get_element_at_index(self, index):
        if not ListAccessor.is_valid_index(index):
            raise ValueError("Index must be a non-negative integer less than MAX_INDEX")
        if index >= len(self.lst):
            raise IndexError("Index out of bounds")
        return self.lst[index]

if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    accessor = ListAccessor(sample_list)
    try:
        index_to_find = 2
        element = accessor.get_element_at_index(index_to_find)
        print(f"Element at index {index_to_find}: {element}")
    except (ValueError, IndexError) as e:
        print(e)