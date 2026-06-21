def get_first_element(lst):
    if not isinstance(lst, list):
        raise ValueError("Input must be a list")
    return lst[0] if lst else None

class ListProcessor:
    def __init__(self, data):
        self.data = data
    
    def first_element(self):
        return get_first_element(self.data)

if __name__ == '__main__':
    sample_data = [
        [1, 2, 3],
        [],
        ['a', 'b', 'c'],
        [True, False],
        [None]
    ]
    
    for data in sample_data:
        processor = ListProcessor(data)
        print(processor.first_element())