class SafeListWrapper:
    def __init__(self, data):
        self._data = data

    def get_second_element(self):
        try:
            return self._data[1]
        except IndexError as e:
            return f"Error: {str(e)}"

if __name__ == '__main__':
    list_a = [1, 2, 3, 4, 5]
    list_b = ['a', 'b']
    list_c = [True]
    list_d = []

    wrapper_a = SafeListWrapper(list_a)
    wrapper_b = SafeListWrapper(list_b)
    wrapper_c = SafeListWrapper(list_c)
    wrapper_d = SafeListWrapper(list_d)

    print(f"Second element of {list_a}: {wrapper_a.get_second_element()}")
    print(f"Second element of {list_b}: {wrapper_b.get_second_element()}")
    print(f"Second element of {list_c}: {wrapper_c.get_second_element()}")
    print(f"Second element of {list_d}: {wrapper_d.get_second_element()}")