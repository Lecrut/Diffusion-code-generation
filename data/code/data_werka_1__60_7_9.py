class ListAccessor:
    def __init__(self, data_list):
        self.data_list = data_list

    def get_last_element(self):
        if not self.data_list:
            raise IndexError("Cannot retrieve the last element from an empty list.")
        return self.data_list[-1]

if __name__ == '__main__':
    list_accessor1 = ListAccessor([1, 2, 3, 4, 5])
    list_accessor2 = ListAccessor([])

    try:
        print(list_accessor1.get_last_element())
    except IndexError as e:
        print(e)

    try:
        print(list_accessor2.get_last_element())
    except IndexError as e:
        print(e)