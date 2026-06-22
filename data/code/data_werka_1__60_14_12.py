class ArrayUtils:
    @staticmethod
    def get_last_element(arr):
        if not arr:
            return None
        return arr[-1]

if __name__ == '__main__':
    sample_data = [10, 20, 30, 40, 50]
    last_item = ArrayUtils.get_last_element(sample_data)
    print("Last item:", last_item)

    empty_list = []
    last_item_empty = ArrayUtils.get_last_element(empty_list)
    print("Last item of empty list:", last_item_empty)

    single_item_list = [100]
    last_item_single = ArrayUtils.get_last_element(single_item_list)
    print("Last item of single item list:", last_item_single)