class ItemComparator:

    def __init__(self, list1, list2):
        self.list1 = list1
        self.list2 = list2

    def find_unique_items(self):
        set1 = set(self.list1)
        set2 = set(self.list2)
        unique_items = set1 - set2
        return list(unique_items)
if __name__ == '__main__':
    sample_list1 = [1, 3, 5, 7, 9]
    sample_list2 = [0, 2, 4, 6, 8]
    comparator = ItemComparator(sample_list1, sample_list2)
    unique_items = comparator.find_unique_items()
    print('Unique items in the first list:', unique_items)