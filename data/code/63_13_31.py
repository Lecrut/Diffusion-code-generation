def get_first_element(lst):
    if not isinstance(lst, list):
        raise ValueError("Input must be a list")
    return lst[0] if lst else None

class ListProcessor:
    def __init__(self, data):
        self.data = data

    def process(self):
        first_elements = []
        for item in self.data:
            first_elements.append(get_first_element(item))
        return first_elements

if __name__ == '__main__':
    sample_data = [
        [10, 20, 30],
        [],
        ['x', 'y', 'z'],
        [True, False],
        [None]
    ]
    
    processor = ListProcessor(sample_data)
    print(processor.process())