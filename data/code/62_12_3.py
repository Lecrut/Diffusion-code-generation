class ListAccessor:
    def __init__(self, data):
        self._data = list(data)
    def get_second(self):
        if len(self._data) > 1:
            return self._data[1]
        else:
            raise IndexError("List does not have a second element")
if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    accessor = ListAccessor(sample_list)
    second_element = accessor.get_second()
    print(second_element)
    sample_list_short = [100]
    accessor_short = ListAccessor(sample_list_short)
    try:
        accessor_short.get_second()
    except IndexError as e:
        print(f"Error caught: {e}")