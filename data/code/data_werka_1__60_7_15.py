class ListUtils:
    @staticmethod
    def get_last_element(data_list):
        if not data_list:
            raise IndexError("Cannot retrieve the last element from an empty list.")
        return data_list[-1]

if __name__ == '__main__':
    list1 = [1, 2, 3, 4, 5]
    list2 = []
    try:
        result1 = ListUtils.get_last_element(list1)
        print(f"Result for list1: {result1}")
    except IndexError as e:
        print(f"Error for list1: {e}")
    try:
        result2 = ListUtils.get_last_element(list2)
        print(f"Result for list2: {result2}")
    except IndexError as e:
        print(f"Error for list2: {e}")