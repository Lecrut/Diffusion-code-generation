class ListHandler:
    EMPTY_LIST_ERROR = "Cannot get the last item from an empty list"

    @staticmethod
    def get_last_item(mutable_list):
        if not mutable_list:
            raise IndexError(ListHandler.EMPTY_LIST_ERROR)
        return mutable_list[-1]

if __name__ == '__main__':
    sample_list1 = [1, 2, 3, 4, 5]
    sample_list2 = []
    
    try:
        print(f"Last item of {sample_list1}: {ListHandler.get_last_item(sample_list1)}")
    except IndexError as e:
        print(e)
    
    try:
        print(f"Last item of {sample_list2}: {ListHandler.get_last_item(sample_list2)}")
    except IndexError as e:
        print(e)