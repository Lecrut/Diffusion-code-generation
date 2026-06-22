class DifferenceFinder:

    def __init__(self, list1: list, list2: list):
        self.list1 = list1
        self.list2 = list2

    def find_difference(self) -> list:
        set1 = set(self.list1)
        set2 = set(self.list2)
        return list(set1 - set2)
if __name__ == '__main__':
    sample_list1 = [5, 7, 9, 10, 12]
    sample_list2 = [9, 10, 11, 13, 15]
    difference_finder = DifferenceFinder(sample_list1, sample_list2)
    result = difference_finder.find_difference()
    print(result)
    another_list1 = [20, 30, 40, 50]
    another_list2 = [30, 40, 60, 70]
    another_difference_finder = DifferenceFinder(another_list1, another_list2)
    another_result = another_difference_finder.find_difference()
    print(another_result)