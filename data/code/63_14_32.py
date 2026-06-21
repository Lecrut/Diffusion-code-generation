class ListProcessor:
    def __init__(self, data):
        self.data = data

    def get_first_element(self):
        if not isinstance(self.data, list):
            raise ValueError('Input must be a list')
        if len(self.data) == 0:
            return None
        return self.data[0]

if __name__ == '__main__':
    sample_list_processor = ListProcessor([1, 2, 3])
    empty_list_processor = ListProcessor([])
    non_list_input_processor = ListProcessor('not a list')

    try:
        print(sample_list_processor.get_first_element())
    except ValueError as e:
        print(e)

    try:
        print(empty_list_processor.get_first_element())
    except ValueError as e:
        print(e)

    try:
        print(non_list_input_processor.get_first_element())
    except ValueError as e:
        print(e)