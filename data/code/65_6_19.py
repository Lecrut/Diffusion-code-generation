class ListAccessor:
    DEFAULT_LIST = [10, 20, 30, 40, 50, 60, 70]
    TARGET_INDEX = 4

    @staticmethod
    def get_element_at_index(lst, index):
        if not isinstance(lst, list):
            raise TypeError("The first argument must be a list.")
        if not isinstance(index, int):
            raise TypeError("The second argument must be an integer.")
        if index < 0 or index >= len(lst):
            raise IndexError("Index out of bounds")
        return lst[index]

if __name__ == '__main__':
    try:
        element = ListAccessor.get_element_at_index(ListAccessor.DEFAULT_LIST, ListAccessor.TARGET_INDEX)
        print(element)
    except (TypeError, IndexError) as e:
        print(e)