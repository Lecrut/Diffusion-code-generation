class ListHandler:
    EMPTY_LIST_ERROR = "The list is empty."

    @staticmethod
    def get_last_item(string_list):
        if not string_list:
            raise ValueError(ListHandler.EMPTY_LIST_ERROR)
        return string_list[-1]

if __name__ == '__main__':
    my_list = ["apple", "banana", "cherry", "date"]
    try:
        last_item = ListHandler.get_last_item(my_list)
        print("The list of strings is:", my_list)
        print("The last item in the list is:", last_item)
    except ValueError as e:
        print(e)

    empty_list = []
    try:
        last_item = ListHandler.get_last_item(empty_list)
        print("The list of strings is:", empty_list)
        print("The last item in the list is:", last_item)
    except ValueError as e:
        print(e)