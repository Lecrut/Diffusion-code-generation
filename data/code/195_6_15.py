class ListComparator:
    KEY = 'key'

    @staticmethod
    def compare_dictionaries(dict1, dict2):
        if dict1.get(ListComparator.KEY) == dict2.get(ListComparator.KEY):
            return True
        else:
            return False

    @staticmethod
    def compare_lists(list1, list2):
        comparison_results = []
        for item1, item2 in zip(list1, list2):
            try:
                if ListComparator.compare_dictionaries(item1, item2):
                    comparison_results.append(True)
                else:
                    comparison_results.append(False)
            except TypeError:
                comparison_results.append("Type Error")
        return comparison_results

if __name__ == '__main__':
    dict_a = {'key': 1}
    dict_b = {'key': 1}
    dict_c = {'key': 2}
    dict_d = {'key': 'a'}

    list_a = [dict_a, dict_b]
    list_b = [dict_a, dict_c]
    list_c = [dict_a, dict_d]

    print("Comparing list_a and list_b:")
    result1 = ListComparator.compare_lists(list_a, list_b)
    print(result1)

    print("Comparing list_a and list_c:")
    result2 = ListComparator.compare_lists(list_a, list_c)
    print(result2)

    print("Comparing list_a and list_d:")
    result3 = ListComparator.compare_lists(list_a, list_d)
    print(result3)