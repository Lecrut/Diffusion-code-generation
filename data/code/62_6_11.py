class SafeListAccess:
    def __init__(self, data):
        self._data = data

    def get_second_element(self):
        if len(self._data) < 2:
            return "IndexError: List does not have a second element"
        return self._data[1]

if __name__ == '__main__':
    sample_list_a = [1, 2, 3]
    sample_list_b = ['a']
    sample_list_c = []
    
    access_a = SafeListAccess(sample_list_a)
    access_b = SafeListAccess(sample_list_b)
    access_c = SafeListAccess(sample_list_c)
    
    print(f"Second element of {sample_list_a}: {access_a.get_second_element()}")
    print(f"Second element of {sample_list_b}: {access_b.get_second_element()}")
    print(f"Second element of {sample_list_c}: {access_c.get_second_element()}")