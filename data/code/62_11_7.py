class ListAccessor:
    def __init__(self, data):
        self.data = data

    def get_second(self):
        if len(self.data) > 1:
            return self.data[1]
        else:
            return None

if __name__ == '__main__':
    list_accessor1 = ListAccessor([10, 20, 30])
    list_accessor2 = ListAccessor([5])
    list_accessor3 = ListAccessor([])
    list_accessor4 = ListAccessor([1])

    print(f"List Accessor 1: {list_accessor1.get_second()}")
    print(f"List Accessor 2: {list_accessor2.get_second()}")
    print(f"List Accessor 3: {list_accessor3.get_second()}")
    print(f"List Accessor 4: {list_accessor4.get_second()}")