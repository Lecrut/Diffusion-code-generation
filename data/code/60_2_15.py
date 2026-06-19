class ListHandler:
    EMPTY_LIST_ERROR = "Cannot get the last item from an empty list"

    @staticmethod
    def get_last_item(data_list):
        if not data_list:
            raise IndexError(ListHandler.EMPTY_LIST_ERROR)
        return data_list[-1]

if __name__ == '__main__':
    sample_list = [5, 10, 15, 20]
    try:
        print(ListHandler.get_last_item(sample_list))
    except IndexError as e:
        print(e)

    empty_list = []
    try:
        print(ListHandler.get_last_item(empty_list))
    except IndexError as e:
        print(e)