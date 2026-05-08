class List:
    def __init__(self, items):
        self.items = list(items)
    def remove_by_value(self, value):
        try:
            index = self.items.index(value)
            del self.items[index]
        except ValueError:
            pass
if __name__ == '__main__':
    data = [1, 5, 2, 8, 5, 3]
    my_list = List(data)
    print("Original list:", my_list.items)
    my_list.remove_by_value(5)
    print("After removing first 5:", my_list.items)
    my_list.remove_by_value(8)
    print("After removing 8:", my_list.items)
    my_list.remove_by_value(99)
    print("After removing non-existent 99:", my_list.items)
    my_list.remove_by_value(2)
    print("After removing 2:", my_list.items)