class SafeListAccess:
    EMPTY_LIST_ERROR_MESSAGE = "Cannot retrieve the first item from an empty list"

    @staticmethod
    def get_first_item_safe(data_list):
        if not data_list:
            raise IndexError(SafeListAccess.EMPTY_LIST_ERROR_MESSAGE)
        return data_list[0]

if __name__ == '__main__':
    list1 = [5, 15, 25]
    list2 = []
    try:
        item1 = SafeListAccess.get_first_item_safe(list1)
        print(f"First item from list1: {item1}")
    except IndexError as e:
        print(f"Error processing list1: {e}")
    try:
        item2 = SafeListAccess.get_first_item_safe(list2)
        print(f"First item from list2: {item2}")
    except IndexError as e:
        print(f"Error processing list2: {e}")