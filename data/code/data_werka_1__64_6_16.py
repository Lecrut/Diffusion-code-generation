class ItemLocator:
    def __init__(self, lst):
        self.lst = lst

    def find_final_item_index(self, item):
        if not self.lst:
            return -1
        for i in range(len(self.lst) - 1, -1, -1):
            if self.lst[i] == item:
                return i
        return -1

if __name__ == '__main__':
    assert ItemLocator([]).find_final_item_index(5) == -1, 'Test case 1 failed'
    assert ItemLocator([1, 2, 3, 4]).find_final_item_index(5) == -1, 'Test case 2 failed'
    assert ItemLocator([1, 2, 3, 4, 3]).find_final_item_index(3) == 4, 'Test case 3 failed'
    assert ItemLocator(['a', 'b', 'c', 'b']).find_final_item_index('b') == 3, 'Test case 4 failed'
    
    sample_list = [10, 20, 30, 40, 50]
    item_to_find = 30
    locator = ItemLocator(sample_list)
    result = locator.find_final_item_index(item_to_find)
    print(result)

    another_sample_list = [7, 8, 9, 10, 11, 9]
    another_item_to_find = 9
    another_locator = ItemLocator(another_sample_list)
    another_result = another_locator.find_final_item_index(another_item_to_find)
    print(another_result)