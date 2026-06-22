class SafeListAccess:
    def __init__(self, data):
        self._data = data

    def get_second_element(self):
        try:
            return self._data[1]
        except IndexError:
            return "IndexError: List does not have a second element"

if __name__ == '__main__':
    list_a = [1, 2, 3, 4]
    list_b = ['a']
    list_c = []

    safe_access_a = SafeListAccess(list_a)
    safe_access_b = SafeListAccess(list_b)
    safe_access_c = SafeListAccess(list_c)

    print(f"Second element of {list_a}: {safe_access_a.get_second_element()}")
    print(f"Second element of {list_b}: {safe_access_b.get_second_element()}")
    print(f"Second element of {list_c}: {safe_access_c.get_second_element()}")