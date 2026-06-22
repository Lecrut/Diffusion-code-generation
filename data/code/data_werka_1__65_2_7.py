class ListUtil:
    INDEX_THIRD = 2

    @staticmethod
    def get_third_element(lst):
        if len(lst) > ListUtil.INDEX_THIRD:
            return lst[ListUtil.INDEX_THIRD]
        raise IndexError("List does not have a third element")

if __name__ == '__main__':
    sample_list = [5, 15, 25, 35, 45]
    try:
        third_element = ListUtil.get_third_element(sample_list)
        print(f"The third element is: {third_element}")
        ListUtil.get_third_element([1, 2])
    except IndexError as e:
        print(e)