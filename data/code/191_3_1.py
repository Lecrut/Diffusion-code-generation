class ListCombiner:
    @staticmethod
    def combine_and_sort(list1, list2):
        combined = list1 + list2
        combined.sort()
        return combined
if __name__ == '__main__':
    list_a = [3, 1, 4]
    list_b = [5, 2, 8]
    result = ListCombiner.combine_and_sort(list_a, list_b)
    print(result)