class ListComparator:
    @staticmethod
    def compare_elements(list1, list2):
        return [f"{x} > {y}" if x > y else f"{x} < {y}" if x < y else f"{x} == {y}" for x, y in zip(list1, list2)]

if __name__ == '__main__':
    sample_list1 = [5, 9, 14, 19]
    sample_list2 = [3, 8, 14, 20]
    comparison_results = ListComparator.compare_elements(sample_list1, sample_list2)
    for result in comparison_results:
        print(result)