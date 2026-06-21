class ListJoiner:
    def join_lists(self, list1, list2):
        return list1 + list2

if __name__ == '__main__':
    joiner = ListJoiner()
    sample_list1 = [1, 2, 3]
    sample_list2 = [4, 5, 6]
    result = joiner.join_lists(sample_list1, sample_list2)
    print(result)