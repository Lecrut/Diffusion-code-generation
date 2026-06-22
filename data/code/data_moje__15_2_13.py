class ListAccessor:
    def __init__(self, items):
        self.items = items

    def get_second_last(self):
        return self.items[-2]

    def get_last(self):
        return self.items[-1]

if __name__ == '__main__':
    numbers = [5, 12, 8, 19, 4, 22]
    accessor = ListAccessor(numbers)
    second_last_val = accessor.get_second_last()
    last_val = accessor.get_last()
    print(second_last_val)
    print(last_val)