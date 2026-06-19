class ItemComparison:
    def __init__(self, list1, list2):
        self.list1 = list1
        self.list2 = list2

    def unique_to_list1(self):
        set1 = set(self.list1)
        set2 = set(self.list2)
        return list(set1 - set2)

    def unique_to_list2(self):
        set1 = set(self.list1)
        set2 = set(self.list2)
        return list(set2 - set1)

if __name__ == '__main__':
    sample_list1 = [1, 2, 3, 4, 5]
    sample_list2 = [4, 5, 6, 7, 8]

    comparator = ItemComparison(sample_list1, sample_list2)
    
    unique_in_list1 = comparator.unique_to_list1()
    unique_in_list2 = comparator.unique_to_list2()

    print("Items unique to list1:", unique_in_list1)
    print("Items unique to list2:", unique_in_list2)