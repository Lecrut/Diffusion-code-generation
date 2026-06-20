class ListComparator:
    @staticmethod
    def compare_lists(list1, list2):
        results = []
        for item1, item2 in zip(list1, list2):
            if item1 > item2:
                results.append(f"{item1} > {item2}")
            elif item1 < item2:
                results.append(f"{item1} < {item2}")
            else:
                results.append(f"{item1} == {item2}")
        return results

if __name__ == '__main__':
    comparator = ListComparator()
    sample_list1 = [5, 10, 15, 20]
    sample_list2 = [3, 10, 20, 25]
    comparison_results = comparator.compare_lists(sample_list1, sample_list2)
    for result in comparison_results:
        print(result)