class CommonItemsFinder:
    @staticmethod
    def unique_common_items(list1, list2):
        set1 = set(list1)
        set2 = set(list2)
        return set1.intersection(set2)

if __name__ == '__main__':
    sample_list1 = [1, 2, 3, 4, 5]
    sample_list2 = [4, 5, 6, 7, 8]
    finder = CommonItemsFinder()
    print(finder.unique_common_items(sample_list1, sample_list2))