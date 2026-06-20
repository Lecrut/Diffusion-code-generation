class ListWrapper:
    def __init__(self, data):
        self._data = data

    def get_edge_elements(self):
        if not self._data:
            return None, None
        return self._data[0], self._data[-1]

if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5]
    wrapper = ListWrapper(sample_list)
    first, last = wrapper.get_edge_elements()
    print(f"First element: {first}")
    print(f"Last element: {last}")

    sample_list_empty = []
    wrapper_empty = ListWrapper(sample_list_empty)
    first_empty, last_empty = wrapper_empty.get_edge_elements()
    print(f"Empty list - First element: {first_empty}, Last element: {last_empty}")