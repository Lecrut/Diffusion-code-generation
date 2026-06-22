class ListHandler:
    def __init__(self, items):
        if not isinstance(items, list):
            raise ValueError("Input must be a list.")
        self.items = items

    def get_last_item(self):
        if not self.items:
            raise IndexError("The list is empty.")
        return self.items[-1]

if __name__ == '__main__':
    sample_list = ["apple", "banana", "cherry", "date"]
    handler = ListHandler(sample_list)
    try:
        last_item = handler.get_last_item()
        print(f"List: {sample_list}")
        print(f"Last item: {last_item}")
    except Exception as e:
        print(e)