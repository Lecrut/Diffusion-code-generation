class ListComparator:

    def __init__(self, list1: list, list2: list):
        self.list1 = set(list1)
        self.list2 = set(list2)

    def find_difference(self) -> list:
        return list(self.list1 - self.list2)
if __name__ == '__main__':
    sample_list1 = [10, 20, 30, 40, 50]
    sample_list2 = [30, 40, 50, 60, 70]
    comparator = ListComparator(sample_list1, sample_list2)
    difference = comparator.find_difference()
    print(difference)
    sample_list3 = [5, 15, 25, 35, 45]
    sample_list4 = [15, 25, 35, 45, 55]
    comparator2 = ListComparator(sample_list3, sample_list4)
    difference2 = comparator2.find_difference()
    print(difference2)