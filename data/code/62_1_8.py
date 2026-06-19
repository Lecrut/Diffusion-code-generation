class ListHandler:
    def __init__(self, items):
        self.items = items

    def get_second_item(self):
        if len(self.items) < 2:
            raise IndexError("List does not have a second item.")
        return self.items[1]

if __name__ == '__main__':
    sample_list = [8, 18, 28]
    handler = ListHandler(sample_list)
    try:
        print(handler.get_second_item())
    except IndexError as e:
        print(e)

    another_list = [42]
    another_handler = ListHandler(another_list)
    try:
        print(another_handler.get_second_item())
    except IndexError as e:
        print(e)