class ListIntersection:
    @staticmethod
    def filter_non_hashable_items(items):
        return [item for item in items if isinstance(item, (int, float, str))]

    @staticmethod
    def find_common_elements(list1, list2):
        filtered_list1 = ListIntersection.filter_non_hashable_items(list1)
        filtered_list2 = ListIntersection.filter_non_hashable_items(list2)
        set1 = set(filtered_list1)
        set2 = set(filtered_list2)
        common_elements = set1.intersection(set2)
        return list(common_elements)

if __name__ == '__main__':
    list_a = [1, 2, 2, 3, 4, 'a', (5, 6)]
    list_b = [3, 4, 'a', (7, 8), 4]
    common = ListIntersection.find_common_elements(list_a, list_b)
    print(common)