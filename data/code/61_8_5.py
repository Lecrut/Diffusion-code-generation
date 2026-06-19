class ListAccessor:
    DEFAULT_LIST = [100, 200, 300, 400, 500]
    DEFAULT_INDEX = 2

    @staticmethod
    def get_element_at_index(lst, index):
        if not isinstance(lst, list):
            raise TypeError("The first argument must be a list")
        if not isinstance(index, int):
            raise TypeError("The second argument must be an integer")
        if index < 0 or index >= len(lst):
            raise IndexError("Index out of bounds")
        return lst[index]

if __name__ == '__main__':
    sample_list = ListAccessor.DEFAULT_LIST
    target_index = ListAccessor.DEFAULT_INDEX
    try:
        result = ListAccessor.get_element_at_index(sample_list, target_index)
        print(result)
    except (TypeError, IndexError) as e:
        print(f"Error: {e}")