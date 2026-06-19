class ListAccessor:
    DEFAULT_LIST = [10, 20, 30, 40, 50, 60, 70]

    @staticmethod
    def get_element_at_index(index):
        if index < 0 or index >= len(ListAccessor.DEFAULT_LIST):
            raise IndexError("Index out of bounds")
        return ListAccessor.DEFAULT_LIST[index]

if __name__ == '__main__':
    target_index = 4
    try:
        element = ListAccessor.get_element_at_index(target_index)
        print(element)
    except IndexError as e:
        print(e)