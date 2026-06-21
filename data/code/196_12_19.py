class ListCombiner:
    @staticmethod
    def combine_lists(list1, list2):
        return list1 + list2

if __name__ == '__main__':
    sample_list_a = ["apple", "banana"]
    sample_list_b = ["cherry", "date"]
    combined_result = ListCombiner.combine_lists(sample_list_a, sample_list_b)
    print(combined_result)