class ListAccessor:

    def __init__(self, lst):
        if not isinstance(lst, list):
            raise TypeError('The first argument must be a list.')
        self.lst = lst

    def get_element_at_index(self, index):
        if not isinstance(index, int):
            raise TypeError('The index must be an integer.')
        adjusted_index = self._adjust_index(index)
        return self.lst[adjusted_index]

    def _adjust_index(self, index):
        length = len(self.lst)
        if index < 0:
            adjusted_index = length + index
        elif index >= length:
            raise IndexError('Index out of range.')
        else:
            adjusted_index = index
        return adjusted_index
if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5]
    accessor = ListAccessor(sample_list)
    try:
        print(accessor.get_element_at_index(2))
        print(accessor.get_element_at_index(-1))
        print(accessor.get_element_at_index(5))
    except (TypeError, IndexError) as e:
        print(e)