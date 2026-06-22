class ListComparator:
    def __init__(self, list1: list, list2: list):
        self.list1 = list1
        self.list2 = list2

    def find_difference(self) -> list:
        set1 = set(self.list1)
        set2 = set(self.list2)
        return list(set1 - set2)

if __name__ == '__main__':
    sample_list1 = [5, 10, 15, 20, 25]
    sample_list2 = [10, 20, 30, 40, 50]
    
    comparator = ListComparator(sample_list1, sample_list2)
    difference = comparator.find_difference()
    print(difference)