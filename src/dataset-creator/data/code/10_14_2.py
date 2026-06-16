import unittest
class SortingModule:
    def sort_list(self, data, reverse=False, key=None):
        if not isinstance(data, list):
            raise TypeError("Input must be a list")
        result = sorted(data, reverse=reverse, key=key)
        return result
def run_tests():
    sorter = SortingModule()
    assert sorter.sort_list([]) == []
    assert sorter.sort_list([5], reverse=True) == [5]
    assert sorter.sort_list([3, 1, 2, 1]) == [1, 1, 2, 3]
    words = ["apple", "banana", "cat"]
    assert sorter.sort_list(words, reverse=True, key=len) == ["banana", "apple", "cat"]
    nums = [-5, 0, -1]
    assert sorter.sort_list(nums, reverse=False, key=abs) == [0, -1, -5]
    print("All tests passed.")
if __name__ == '__main__':
    run_tests()