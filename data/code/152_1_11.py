class ListIntersection:
    @staticmethod
    def find_common_elements(list1, list2):
        seen = set()
        common_elements = []
        for item in list1:
            if item in list2 and item not in seen:
                common_elements.append(item)
                seen.add(item)
        return common_elements

if __name__ == '__main__':
    sample_list1 = [1, 2, 3, 4, 5]
    sample_list2 = [4, 5, 6, 7, 8]
    result = ListIntersection.find_common_elements(sample_list1, sample_list2)
    print(f"Common elements between {sample_list1} and {sample_list2}: {result}")