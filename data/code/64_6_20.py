class ItemLocator:
    def __init__(self, lst):
        self.lst = lst

    def find_final_item_index(self, item):
        index = -1
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
    print(locator.find_final_item_index(item_to_find))