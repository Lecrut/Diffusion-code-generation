class List:
    def __init__(self, initial_list):
        self.data = list(initial_list)
    def remove_by_value(self, value):
        try:
            index = self.data.index(value)
            self.data.pop(index)
        except ValueError:
            pass
if __name__ == '__main__':
    my_list = List([10, 20, 30, 20, 40, 20])
    print("Original list:", my_list.data)
    my_list.remove_by_value(20)
    print("After removing one instance of 20:", my_list.data)
    my_list.remove_by_value(10)
    print("After removing 10:", my_list.data)
    my_list.remove_by_value(99)
    print("After removing 99 (not found):", my_list.data)
    my_list.remove_by_value(40)
    print("After removing 40:", my_list.data)