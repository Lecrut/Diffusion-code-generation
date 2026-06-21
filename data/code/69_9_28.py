class IndexAccessor:
    def __init__(self):
        self.error_messages = {
            'type_error_list': "The first argument must be a list.",
            'type_error_index': "The index must be an integer.",
            'index_error': "Index out of bounds."
        }

    def get_element(self, data_list, index):
        if not isinstance(data_list, list):
            raise TypeError(self.error_messages['type_error_list'])
        if not isinstance(index, int):
            raise TypeError(self.error_messages['type_error_index'])
        try:
            return data_list[index]
        except IndexError:
            raise IndexError(self.error_messages['index_error'])

if __name__ == '__main__':
    accessor = IndexAccessor()
    sample_list = [10, 20, 30, 40, 50]
    index_to_access = 2
    try:
        element = accessor.get_element(sample_list, index_to_access)
        print(f"Element at index {index_to_access}: {element}")
    except Exception as e:
        print(e)