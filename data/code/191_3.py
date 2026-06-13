class ListCombiner:
    @staticmethod
    def combine_and_sort(list1, list2):
        combined_list = list1 + list2
        combined_list.sort()
        return combined_list
if __name__ == '__main__':
    list_a = [5, 1, 8]
    list_b = [3, 7, 2]
    result = ListCombiner.combine_and_sort(list_a, list_b)
    print(result)