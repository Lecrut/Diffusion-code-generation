class ListAccessor:
    def __init__(self, data_list):
        self.data_list = data_list

    def get_last_element(self):
        if not self.data_list:
            raise IndexError("Cannot get the last element from an empty list.")
        return self.data_list[-1]

if __name__ == '__main__':
    list1 = [10, 20, 30, 40, 50]
    list2 = []

    accessor1 = ListAccessor(list1)
    try:
        print(accessor1.get_last_element())
    except IndexError as e:
        print(e)

    accessor2 = ListAccessor(list2)
    try:
        print(accessor2.get_last_element())
    except IndexError as e:
        print(e)