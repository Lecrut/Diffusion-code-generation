class ListAccessor:
    DEFAULT_LIST = [10, 20, 30, 40, 50, 60, 70]

    @staticmethod
    def get_element_at_index(lst, index):
        if not isinstance(index, int) or index < 0 or index >= len(lst):
            raise IndexError("Index out of bounds")
        return lst[index]

if __name__ == '__main__':
    target_index = 4
    try:
        element = ListAccessor.get_element_at_index(ListAccessor.DEFAULT_LIST, target_index)
        print(element)
    except IndexError as e:
        print(e)