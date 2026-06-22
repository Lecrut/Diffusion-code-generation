class ListUtils:
    EMPTY_LIST_MESSAGE = "list is empty"

    @staticmethod
    def get_last_item(data):
        if not data:
            raise IndexError(ListUtils.EMPTY_LIST_MESSAGE)
        return data[-1]

if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    try:
        last_element = ListUtils.get_last_item(sample_list)
        print(last_element)
    except IndexError as e:
        print(e)

    empty_list = []
    try:
        ListUtils.get_last_item(empty_list)
    except IndexError as e:
        print(f"Error for empty list: {e}")