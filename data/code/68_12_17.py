class ListComparator:
    def __init__(self, list1: list, list2: list):
        self.list1 = list1
        self.list2 = list2

    @staticmethod
    def _convert_to_set(lst: list) -> set:
        return set(lst)

    def find_difference(self) -> list:
        set1 = self._convert_to_set(self.list1)
        set2 = self._convert_to_set(self.list2)
        difference_set = set1 - set2
        return list(difference_set)

if __name__ == '__main__':
    sample_list1 = [5, 7, 9, 10, 12]
    sample_list2 = [9, 10, 12, 14, 16]
    comparator = ListComparator(sample_list1, sample_list2)
    result = comparator.find_difference()
    print(result)