class ListHandler:
    def __init__(self, data):
        self.data = data

    def get_first_element(self):
        if not isinstance(self.data, list):
            raise ValueError('Input must be a list')
        if len(self.data) == 0:
            return None
        return self.data[0]

if __name__ == '__main__':
    sample_list_handler = ListHandler([1, 2, 3])
    empty_list_handler = ListHandler([])
    non_list_input_handler = ListHandler('not a list')

    try:
        print(sample_list_handler.get_first_element())
    except ValueError as e:
        print(e)

    try:
        print(empty_list_handler.get_first_element())
    except ValueError as e:
        print(e)

    try:
        print(non_list_input_handler.get_first_element())
    except ValueError as e:
        print(e)