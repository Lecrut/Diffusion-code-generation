class SafeListAccess:
    def __init__(self, data_list):
        if not isinstance(data_list, list):
            raise TypeError("Input must be a list.")
        self.data_list = data_list

    def get_last_element(self):
        if not self.data_list:
            raise IndexError("Cannot get the last element from an empty list.")
        return self.data_list[-1]

if __name__ == '__main__':
    sample_list1 = [1, 2, 3, 4, 5]
    sample_list2 = []

    try:
        safe_access1 = SafeListAccess(sample_list1)
        print(f"Result for sample_list1: {safe_access1.get_last_element()}")
    except (IndexError, TypeError) as e:
        print(f"Error for sample_list1: {e}")

    try:
        safe_access2 = SafeListAccess(sample_list2)
        print(f"Result for sample_list2: {safe_access2.get_last_element()}")
    except (IndexError, TypeError) as e:
        print(f"Error for sample_list2: {e}")