class ListHelper:
    @staticmethod
    def get_last_element(data_list):
        if not data_list:
            raise IndexError("Cannot retrieve the last element from an empty list.")
        return data_list[-1]

if __name__ == '__main__':
    sample_list1 = [1, 2, 3, 4, 5]
    sample_list2 = []

    try:
        result1 = ListHelper.get_last_element(sample_list1)
        print(f"Result for sample_list1: {result1}")
    except IndexError as e:
        print(f"Error for sample_list1: {e}")

    try:
        result2 = ListHelper.get_last_element(sample_list2)
        print(f"Result for sample_list2: {result2}")
    except IndexError as e:
        print(f"Error for sample_list2: {e}")