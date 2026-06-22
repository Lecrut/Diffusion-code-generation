class ListComparator:
    def __init__(self, list1, list2):
        self.list1 = list1
        self.list2 = list2

    def find_unique_items(self):
        set1 = set(self.list1)
        set2 = set(self.list2)
        unique_items = set1 - set2
        return list(unique_items)

if __name__ == '__main__':
    sample_list1 = [1, 2, 3, 4, 5]
    sample_list2 = [4, 5, 6, 7, 8]
    
    comparator = ListComparator(sample_list1, sample_list2)
    unique_items = comparator.find_unique_items()
    print(unique_items)