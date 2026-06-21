class ListExtender:
    @staticmethod
    def extend_lists(list1, list2):
        extended_list = list1 + list2
        return extended_list

if __name__ == '__main__':
    sample_list1 = [{'a': 1}, {'b': 2}]
    sample_list2 = [{'c': 3}, {'d': 4}]
    extender = ListExtender()
    result = extender.extend_lists(sample_list1, sample_list2)
    print(result)