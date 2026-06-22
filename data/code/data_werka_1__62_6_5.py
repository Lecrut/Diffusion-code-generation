class ListAccessWrapper:
    def __init__(self, data):
        self._data = data

    def get_second_element(self):
        try:
            return self._data[1]
        except IndexError:
            return "Error: The list does not contain a second element"

if __name__ == '__main__':
    sample_lists = {
        'list_1': [1, 2, 3],
        'list_2': [45],
        'list_3': [],
        'list_4': ['a', 'b', 'c']
    }

    for name, lst in sample_lists.items():
        wrapper = ListAccessWrapper(lst)
        result = wrapper.get_second_element()
        print(f"Result for {name}: {result}")