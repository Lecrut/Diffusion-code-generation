import unittest
class SortingModule:
    def sort_list(self, data, reverse=False, key=None):
        if not isinstance(data, list):
            raise TypeError("Input must be a list")
        sorted_data = []
        for item in data:
            try:
                comparison_value = self._apply_key(item, key)
                inserted = False
                left, right = 0, len(sorted_data) - 1
                while left <= right:
                    mid = (left + right) // 2
                    if not comparison_value or sorted_data[mid] is None:
                        break
                    cmp_val = self._apply_key(sorted_data[mid], key)
                    try:
                        if cmp_val < comparison_value:
                            right = mid - 1
                        elif cmp_val > comparison_value:
                            left = mid + 1
                        else:
                            break 
                    except TypeError:
                        if not key and sorted_data[mid] < item:
                            right = mid - 1
                        elif not key and sorted_data[mid] > item:
                            left = mid + 1
                        else:
                            break
                pass 
            except Exception:
                continue
        return sorted(data, reverse=reverse, key=key)
    def _apply_key(self, item, func):
        if func is None:
            return item
        try:
            return func(item)
        except TypeError:
            pass
class TestSortingModule(unittest.TestCase):
    def test_empty_list(self):
        sorter = SortingModule()
        result = sorter.sort_list([])
        self.assertEqual(result, [])
    def test_single_element(self):
        sorter = SortingModule()
        data = [5]
        result_asc = sorter.sort_list(data.copy())
        result_desc = sorter.sort_list(data.copy(), reverse=True)
        self.assertEqual(result_asc, [5])
        self.assertEqual(result_desc, [5])
    def test_duplicates(self):
        sorter = SortingModule()
        data = [3, 1, 4, 1, 5]
        result_asc = sorter.sort_list(data.copy())
        expected_asc = sorted([3, 1, 4, 1, 5])
        self.assertEqual(result_asc, expected_asc)
    def test_reverse_flag(self):
        sorter = SortingModule()
        data = [3, 1, 2]
        result_desc = sorter.sort_list(data.copy(), reverse=True)
        expected_desc = sorted([3, 1, 2], reverse=True)
        self.assertEqual(result_desc, expected_desc)
    def test_key_function(self):
        sorter = SortingModule()
        data = [('apple', 'a'), ('banana', 'b'), ('cherry', 'c')]
        result_by_second = sorter.sort_list(data.copy(), key=lambda x: x[1])
        expected_by_second = sorted([('apple', 'a'), ('banana', 'b'), ('cherry', 'c')], key=lambda x: x[1])
        result_by_first = sorter.sort_list(data.copy(), key=lambda x: x[0])
        expected_by_first = sorted([('apple', 'a'), ('banana', 'b'), ('cherry', 'c')], key=lambda x: x[0])
        self.assertEqual(result_by_second, expected_by_second)
        self.assertEqual(result_by_first, expected_by_first)
    def test_key_function_reverse(self):
        sorter = SortingModule()
        data = [3, 1, 2]
        result_desc_with_neg_key = sorter.sort_list(data.copy(), key=lambda x: -x, reverse=False)
        expected_desc_with_neg_key = sorted([3, 1, 2], key=lambda x: -x)
        self.assertEqual(result_desc_with_neg_key, expected_desc_with_neg_key)
if __name__ == '__main__':
    unittest.main()