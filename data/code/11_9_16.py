import operator

class ListAccessor:
    def __init__(self, data):
        self._data = data
        self._getter = operator.itemgetter(-1)

    def get_last(self):
        if not self._data:
            raise IndexError("List is empty, cannot retrieve the last item")
        return self._getter(self._data)

if __name__ == '__main__':
    sample_values = [3.14, 2.71, 1.41, 1.73, 2.23]
    accessor = ListAccessor(sample_values)
    print(accessor.get_last())
    empty_list = []
    try:
        empty_accessor = ListAccessor(empty_list)
        empty_accessor.get_last()
    except IndexError as e:
        print(e)