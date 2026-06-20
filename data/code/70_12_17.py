class ListEdgeGetter:
    def __init__(self, data):
        self._data = data

    def get_edge_elements(self):
        if not self._data:
            return None, None
        first = self._data[0]
        last = self._data[-1]
        return first, last

if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    edge_getter = ListEdgeGetter(sample_list)
    first, last = edge_getter.get_edge_elements()
    print(f"First element: {first}")
    print(f"Last element: {last}")

    sample_list_empty = []
    edge_getter_empty = ListEdgeGetter(sample_list_empty)
    first_empty, last_empty = edge_getter_empty.get_edge_elements()
    print(f"First element (empty list): {first_empty}")
    print(f"Last element (empty list): {last_empty}")