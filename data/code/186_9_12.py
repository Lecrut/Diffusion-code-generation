import functools

class ListSorter:
    @staticmethod
    def sum_elements(lst):
        return sum(lst)

    @staticmethod
    def compare_lists(list1, list2):
        return ListSorter.sum_elements(list1) - ListSorter.sum_elements(list2)

    @classmethod
    def sort_by_sum(cls, lists):
        key = functools.cmp_to_key(cls.compare_lists)
        return sorted(lists, key=key)

if __name__ == '__main__':
    sample_data = [[3, 5], [1, 2], [4, 6]]
    sorter = ListSorter()
    sorted_data = sorter.sort_by_sum(sample_data)
    print(sorted_data)