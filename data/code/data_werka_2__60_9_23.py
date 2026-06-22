class ListUtils:
    EMPTY_LIST_ERROR = "The list is empty"

    @staticmethod
    def get_last_item(lst):
        if not lst:
            raise ValueError(ListUtils.EMPTY_LIST_ERROR)
        return lst[-1]

if __name__ == '__main__':
    sample_list_1 = [10, 20, 30, 40, 50]
    try:
        print("Last item in sample_list_1:", ListUtils.get_last_item(sample_list_1))
    except ValueError as e:
        print(e)

    empty_list = []
    try:
        print("Last item in empty_list:", ListUtils.get_last_item(empty_list))
    except ValueError as e:
        print(e)

    sample_list_2 = ["a", "b", "c", "d"]
    try:
        print("Last item in sample_list_2:", ListUtils.get_last_item(sample_list_2))
    except ValueError as e:
        print(e)