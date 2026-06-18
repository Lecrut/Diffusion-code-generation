import unittest
class SortingModule:
    def sort_list(self, data, reverse=False):
        return sorted(data, reverse=reverse)
def test_sorting_module():
    sorter = SortingModule()
    assert sorter.sort_list([]) == []
    assert sorter.sort_list([5], reverse=True) == [5]
    assert sorter.sort_list([3, 1, 2, 1]) == [1, 1, 2, 3]
    assert sorter.sort_list([3, 1, 2, 1], reverse=True) == [3, 2, 1, 1]
    result = sorter.sort_list(["apple", "banana", "kiwi"], key=len)
    assert result == ["kiwi", "apple", "banana"]
    data_with_key = [3, 1, 2]
    sorted_by_neg = sorter.sort_list(data_with_key, key=lambda x: -x)
    assert sorted_by_neg == [1, 2, 3]
    data_mixed_ints = [50, 10, 75, 25]
    result_asc = sorter.sort_list(data_mixed_ints)
    assert result_asc == [10, 25, 50, 75]
    result_desc = sorter.sort_list(data_mixed_ints, reverse=True)
    assert result_desc == [75, 50, 25, 10]
if __name__ == '__main__':
    unittest.main()