class ListSearcher:
    @staticmethod
    def find_last_occurrence(lst, element):
        for index in range(len(lst) - 1, -1, -1):
            if lst[index] == element:
                return index
        return -1

if __name__ == '__main__':
    sample_list = [7, 8, 9, 7, 10, 7]
    target_element = 7
    result = ListSearcher.find_last_occurrence(sample_list, target_element)
    print(result)

    empty_list = []
    not_found_target = 5
    empty_result = ListSearcher.find_last_occurrence(empty_list, not_found_target)
    print(empty_result)

    single_element_list = [1]
    single_target = 1
    single_result = ListSearcher.find_last_occurrence(single_element_list, single_target)
    print(single_result)

    multiple_elements_list = [2, 3, 4, 5, 2, 6, 2]
    multiple_target = 2
    multiple_result = ListSearcher.find_last_occurrence(multiple_elements_list, multiple_target)
    print(multiple_result)

    non_existent_target = 100
    non_existent_result = ListSearcher.find_last_occurrence(sample_list, non_existent_target)
    print(non_existent_result)