class FloatListManager:
    def __init__(self, initial_list):
        self.lst = initial_list

    def remove_value(self, value):
        for i in range(len(self.lst) - 1, -1, -1):
            if self.lst[i] == value:
                del self.lst[i]
                break

if __name__ == '__main__':
    manager = FloatListManager([3.14, 2.718, 1.618, 2.718, 0.577])
    value_to_remove = 2.718
    manager.remove_value(value_to_remove)
    print(manager.lst)