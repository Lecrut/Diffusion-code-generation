class ListReverser:
    def __init__(self, initial_list=None):
        self._list = initial_list if initial_list is not None else []

    def append(self, value):
        self._list.append(value)

    def reverse(self):
        self._list.reverse()

    def get_list(self):
        return self._list

if __name__ == '__main__':
    reverser = ListReverser()
    for i in range(1, 6):
        reverser.append(i)
    print('Original list:', reverser.get_list())
    reverser.reverse()
    print('Reversed list:', reverser.get_list())