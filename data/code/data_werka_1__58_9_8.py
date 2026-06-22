class SafeListAccess:
    def __init__(self, data):
        self._data = data

    def get_first_element(self):
        if not self._data:
            raise IndexError("The list is empty")
        return self._data[0]

if __name__ == '__main__':
    sample_list = [15, 25, 35, 45]
    try:
        safe_access = SafeListAccess(sample_list)
        first_element = safe_access.get_first_element()
        print(first_element)
    except IndexError as e:
        print(e)

    empty_list = []
    try:
        safe_empty_access = SafeListAccess(empty_list)
        first_empty = safe_empty_access.get_first_element()
        print(first_empty)
    except IndexError as e:
        print(e)