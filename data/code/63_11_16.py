class ListHandler:
    def __init__(self, data):
        if not data:
            raise ValueError("Input list cannot be empty")
        self.data = data

    def get_first_element(self):
        return self.data[0]

if __name__ == '__main__':
    list1 = [1, 2, 3, 4]
    list2 = ['a', 'b', 'c']
    try:
        handler1 = ListHandler(list1)
        print(f"First element of {list1}: {handler1.get_first_element()}")
        handler2 = ListHandler(list2)
        print(f"First element of {list2}: {handler2.get_first_element()}")
    except ValueError as e:
        print(f"Caught expected error: {e}")