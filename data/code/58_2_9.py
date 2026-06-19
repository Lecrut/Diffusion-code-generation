class ListHandler:
    def __init__(self, data_list):
        self.data_list = data_list

    def get_first_item(self):
        if not self.data_list:
            raise IndexError("Cannot retrieve the first item from an empty list")
        return self.data_list[0]

if __name__ == '__main__':
    handler1 = ListHandler([10, 20, 30])
    handler2 = ListHandler([])

    try:
        print(f"First item from list1: {handler1.get_first_item()}")
    except IndexError as e:
        print(f"Error processing list1: {e}")

    try:
        print(f"First item from list2: {handler2.get_first_item()}")
    except IndexError as e:
        print(f"Error processing list2: {e}")