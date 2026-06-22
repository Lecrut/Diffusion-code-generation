class ListAccessor:
    def __init__(self, lst):
        if not isinstance(lst, list):
            raise TypeError('The first argument must be a list.')
        self.lst = lst

    def get_element_at_index(self, index):
        if not isinstance(index, int):
            raise TypeError('The index must be an integer.')
        length = len(self.lst)
        adjusted_index = index % length if index >= 0 else (index + length) % length
        if adjusted_index < 0 or adjusted_index >= length:
            raise IndexError('Index out of range.')
        return self.lst[adjusted_index]

if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    accessor = ListAccessor(sample_list)
    try:
        print(accessor.get_element_at_index(2))
        print(accessor.get_element_at_index(-1))
        print(accessor.get_element_at_index(5))
    except (TypeError, IndexError) as e:
        print(e)