class ListHandler:
    def __init__(self, data):
        self.data = data

    def get_first_element(self):
        if not self.data:
            raise IndexError("The list is empty")
        return self.data[0]

if __name__ == '__main__':
    sample_list = [5, 15, 25, 35]
    handler = ListHandler(sample_list)
    try:
        print(handler.get_first_element())
    except IndexError as e:
        print(e)

    empty_list = []
    empty_handler = ListHandler(empty_list)
    try:
        print(empty_handler.get_first_element())
    except IndexError as e:
        print(e)