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
    print(f"Original list: {my_list.data}")
    my_list.remove_by_value(20)
    print(f"After removing one instance of 20: {my_list.data}")
    my_list.remove_by_value(40)
    print(f"After removing 40: {my_list.data}")
    my_list.remove_by_value(99)
    print(f"After attempting to remove 99: {my_list.data}")
    my_list.remove_by_value(20)
    print(f"After removing another 20: {my_list.data}")