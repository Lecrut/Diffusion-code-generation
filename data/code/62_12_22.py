class ListAccessor:
    def __init__(self, items):
        self.items = items

    def fetch_second(self):
        if len(self.items) < 2:
            raise IndexError("The list does not contain a second element.")
        return self.items[1]

if __name__ == '__main__':
    my_list = [10, 20, 30, 40]
    accessor = ListAccessor(my_list)
    try:
        print(accessor.fetch_second())
    except IndexError as e:
        print(e)

    # Additional test cases
    short_list = [5, 15]
    short_accessor = ListAccessor(short_list)
    try:
        print(short_accessor.fetch_second())
    except IndexError as e:
        print(e)

    single_element_list = [7]
    single_accessor = ListAccessor(single_element_list)
    try:
        print(single_accessor.fetch_second())
    except IndexError as e:
        print(e)

    empty_list = []
    empty_accessor = ListAccessor(empty_list)
    try:
        print(empty_accessor.fetch_second())
    except IndexError as e:
        print(e)