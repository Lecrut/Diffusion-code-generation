class ListHandler:
    EMPTY_LIST_ERROR = "The input list is empty"

    @staticmethod
    def get_first_element(lst):
        if not lst:
            raise ValueError(ListHandler.EMPTY_LIST_ERROR)
        return lst[0]

if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5]
    try:
        print(ListHandler.get_first_element(sample_list))
    except ValueError as e:
        print(e)

    empty_list = []
    try:
        print(ListHandler.get_first_element(empty_list))
    except ValueError as e:
        print(e)

    single_element_list = [42]
    try:
        print(ListHandler.get_first_element(single_element_list))
    except ValueError as e:
        print(e)