class ListUtils:
    SECOND_ITEM_INDEX = 1

    @staticmethod
    def get_second_item(lst):
        if len(lst) < ListUtils.SECOND_ITEM_INDEX + 1:
            raise IndexError("List does not have a second item.")
        return lst[ListUtils.SECOND_ITEM_INDEX]

if __name__ == '__main__':
    sample_list = [9, 19, 29]
    try:
        print(ListUtils.get_second_item(sample_list))
    except IndexError as e:
        print(e)