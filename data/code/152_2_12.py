class UniqueItemsFinder:
    @staticmethod
    def find_common_items(list1, list2):
        common_set = set()
        for item in list1:
            if item in list2 and item not in common_set:
                common_set.add(item)
        return list(common_set)

if __name__ == '__main__':
    sample_list1 = [1, 2, 3, 4, 5]
    sample_list2 = [4, 5, 6, 7, 8]
    finder = UniqueItemsFinder()
    print(finder.find_common_items(sample_list1, sample_list2))