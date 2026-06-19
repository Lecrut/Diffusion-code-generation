class ListAccessor:
    def __init__(self, elements):
        self.elements = elements

    def get_second(self):
        if len(self.elements) < 2:
            raise IndexError("List does not contain at least two elements.")
        return self.elements[1]

if __name__ == '__main__':
    my_list = [10, 20, 30, 40]
    accessor = ListAccessor(my_list)
    print(accessor.get_second())