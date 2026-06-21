class ListComparator:
    @staticmethod
    def count_common_elements(list1, list2):
        return len(set(list1) & set(list2))

if __name__ == '__main__':
    list_a = ["apple", "banana", "cherry", "date"]
    list_b = ["apple", "orange", "cherry", "grape"]
    common_count = ListComparator.count_common_elements(list_a, list_b)
    print(common_count)