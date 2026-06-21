class FloatListManager:
    def __init__(self, initial_list):
        self.float_list = initial_list

    def remove_float(self, value):
        for i in range(len(self.float_list) - 1, -1, -1):
            if self.float_list[i] == value:
                del self.float_list[i]
                break

if __name__ == '__main__':
    manager = FloatListManager([3.14, 2.718, 1.618, 2.718, 0.577])
    manager.remove_float(2.718)
    print(manager.float_list)