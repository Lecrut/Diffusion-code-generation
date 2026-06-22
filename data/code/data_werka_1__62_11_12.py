class ListAccessor:
    def __init__(self, data):
        self.data = data

    def _validate_data(self):
        return len(self.data) > 1

    def get_second(self):
        if self._validate_data():
            return self.data[1]
        else:
            return None

if __name__ == '__main__':
    list1 = [10, 20, 30]
    list2 = [5]
    list3 = []
    list4 = [1]

    accessor1 = ListAccessor(list1)
    accessor2 = ListAccessor(list2)
    accessor3 = ListAccessor(list3)
    accessor4 = ListAccessor(list4)

    print(f"List {list1}: {accessor1.get_second()}")
    print(f"List {list2}: {accessor2.get_second()}")
    print(f"List {list3}: {accessor3.get_second()}")
    print(f"List {list4}: {accessor4.get_second()}")