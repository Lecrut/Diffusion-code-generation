class ListAccessor:
    def __init__(self, items):
        if len(items) < 2:
            raise ValueError("List must contain at least two elements.")
        self.items = items

    def get_second_item(self):
        return self.items[1]

if __name__ == '__main__':
    try:
        sample_list = [5, 15, 25, 35, 45]
        accessor = ListAccessor(sample_list)
        second_item = accessor.get_second_item()
        print(second_item)
    except ValueError as e:
        print(e)