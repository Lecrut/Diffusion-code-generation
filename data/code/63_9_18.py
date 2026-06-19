class ListHandler:
    def __init__(self, data_list):
        self.data_list = data_list

    def get_first_element(self):
        if not self.data_list:
            raise ValueError("The list is empty")
        return self.data_list[0]

if __name__ == '__main__':
    sample_data = [10, 20, 30, 40]
    handler = ListHandler(sample_data)
    print(handler.get_first_element())

    sample_data_empty = []
    handler_empty = ListHandler(sample_data_empty)
    try:
        print(handler_empty.get_first_element())
    except ValueError as e:
        print(e)

    sample_data_single = [99]
    handler_single = ListHandler(sample_data_single)
    print(handler_single.get_first_element())