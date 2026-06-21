class ListJoiner:
    def combine_lists(self, list1, list2):
        return list1 + list2

if __name__ == '__main__':
    joiner = ListJoiner()
    sample_list_a = [1, 2, 3]
    sample_list_b = [4, 5, 6]
    combined_result = joiner.combine_lists(sample_list_a, sample_list_b)
    print(combined_result)