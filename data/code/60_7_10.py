class ListAccessor:
    def __init__(self, data_list):
        self.data_list = data_list

    def get_last_element(self):
        if not self.data_list:
            raise IndexError("Cannot get the last element from an empty list.")
        return self.data_list[-1]

if __name__ == '__main__':
    list1 = [1, 2, 3, 4, 5]
    list2 = []
    
    accessor1 = ListAccessor(list1)
    try:
        print(f"Result for list1: {accessor1.get_last_element()}")
    except IndexError as e:
        print(f"Error for list1: {e}")

    accessor2 = ListAccessor(list2)
    try:
        print(f"Result for list2: {accessor2.get_last_element()}")
    except IndexError as e:
        print(f"Error for list2: {e}")