class Finder:
    NOT_FOUND = -1

    @staticmethod
    def find_final_item_index(lst, item):
        index = Finder.NOT_FOUND
        for i in range(len(lst) - 1, -1, -1):
            if lst[i] == item:
                return i
        return Finder.NOT_FOUND

if __name__ == '__main__':
    assert Finder.find_final_item_index([], 5) == Finder.NOT_FOUND, 'Test case 1 failed'
    assert Finder.find_final_item_index([1, 2, 3, 4], 5) == Finder.NOT_FOUND, 'Test case 2 failed'
    assert Finder.find_final_item_index([1, 2, 3, 4, 3], 3) == 4, 'Test case 3 failed'
    assert Finder.find_final_item_index(['a', 'b', 'c', 'b'], 'b') == 3, 'Test case 4 failed'
    sample_list = [10, 20, 30, 40, 50]
    item_to_find = 30
    print(Finder.find_final_item_index(sample_list, item_to_find))