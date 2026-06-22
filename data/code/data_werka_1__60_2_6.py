class ListHandler:
    def __init__(self, data_list):
        self.data_list = data_list

    def get_last_item(self):
        if not self.data_list:
            raise IndexError("Cannot get the last item from an empty list")
        return self.data_list[-1]

if __name__ == '__main__':
    handler1 = ListHandler([5, 6, 7, 8, 9])
    try:
        print(handler1.get_last_item())
    except IndexError as e:
        print(e)

    handler2 = ListHandler([])
    try:
        print(handler2.get_last_item())
    except IndexError as e:
        print(e)