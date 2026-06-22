MAX_LIST_SIZE = 100
SAMPLE_DATA = [7, 14, 21, 28, 35]

def get_leading_element(items):
    if len(items) == 0:
        raise IndexError("Cannot retrieve leading element from an empty list")
    if len(items) > MAX_LIST_SIZE:
        raise ValueError(f"List size exceeds maximum allowed size of {MAX_LIST_SIZE}")
    return items[0]

class ListAccessor:
    def __init__(self, data):
        self._data = data
    
    def get_head(self):
        return get_leading_element(self._data)

if __name__ == '__main__':
    result = get_leading_element(SAMPLE_DATA)
    print(result)
    accessor = ListAccessor(SAMPLE_DATA)
    print(accessor.get_head())