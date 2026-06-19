class ListHandler:
    def __init__(self, data):
        self.data = data
    
    def get_first_element(self):
        if not self.data:
            raise IndexError("List is empty")
        return self.data[0]

if __name__ == '__main__':
    sample_list = [5, 15, 25, 35]
    handler = ListHandler(sample_list)
    try:
        first = handler.get_first_element()
        print(first)
    except IndexError as e:
        print(e)

    empty_list_handler = ListHandler([])
    try:
        first_empty = empty_list_handler.get_first_element()
        print(first_empty)
    except IndexError as e:
        print(e)