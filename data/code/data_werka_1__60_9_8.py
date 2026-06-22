class ListHandler:
    def __init__(self, items):
        self.items = items

    def get_last_item(self):
        if not self.items:
            raise ValueError("The list is empty.")
        return self.items[-1]

if __name__ == '__main__':
    sample_list = ["apple", "banana", "cherry", "date", "elderberry"]
    handler = ListHandler(sample_list)
    try:
        last_item = handler.get_last_item()
        print("The list of strings is:", sample_list)
        print("The last item in the list is:", last_item)
    except ValueError as e:
        print(e)

    empty_list_handler = ListHandler([])
    try:
        last_item_empty = empty_list_handler.get_last_item()
        print("The last item in the empty list is:", last_item_empty)
    except ValueError as e:
        print(e)