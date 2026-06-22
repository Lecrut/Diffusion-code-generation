MIN_LIST_LENGTH = 2
DEFAULT_SAMPLE_DATA = [100, 200, 300, 400, 500]

def get_second_to_last_element(sequence):
    if len(sequence) < MIN_LIST_LENGTH:
        raise IndexError("Sequence must contain at least two elements")
    return sequence[-2]

class ListAccessor:
    def __init__(self, data):
        self.data = data

    def retrieve_second_to_last(self):
        return get_second_to_last_element(self.data)

if __name__ == '__main__':
    test_values = [1, 2, 3, 4, 5]
    accessor = ListAccessor(test_values)
    print(accessor.retrieve_second_to_last())
    
    sample_values = DEFAULT_SAMPLE_DATA
    print(get_second_to_last_element(sample_values))