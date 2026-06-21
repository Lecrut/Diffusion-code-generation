class ListComparator:
    @staticmethod
    def find_common_elements(list1, list2):
        common = []
        seen_in_list1 = set()
        for item in list1:
            if item in list2 and item not in seen_in_list1:
                common.append(item)
                seen_in_list1.add(item)
        return common

if __name__ == '__main__':
    comparator = ListComparator()
    sample_list1 = [1, 2, 3, 4, 5]
    sample_list2 = [4, 5, 6, 7, 8]
    result = comparator.find_common_elements(sample_list1, sample_list2)
    print(f"Common elements between {sample_list1} and {sample_list2}: {result}")