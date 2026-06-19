class ListHandler:
    def __init__(self, data):
        self.data = data

    def get_first_element(self):
        if not self.data:
            raise IndexError("list is empty")
        return self.data[0]

if __name__ == '__main__':
    list1 = [5, 6, 7, 8]
    list2 = ['x', 'y', 'z']
    empty_list = []

    handler1 = ListHandler(list1)
    try:
        print(f"First element of {list1}: {handler1.get_first_element()}")
    except IndexError as e:
        print(f"Error caught for {list1}: {e}")

    handler2 = ListHandler(list2)
    try:
        print(f"First element of {list2}: {handler2.get_first_element()}")
    except IndexError as e:
        print(f"Error caught for {list2}: {e}")

    handler3 = ListHandler(empty_list)
    try:
        print(f"First element of {empty_list}: {handler3.get_first_element()}")
    except IndexError as e:
        print(f"Error caught for empty list: {e}")