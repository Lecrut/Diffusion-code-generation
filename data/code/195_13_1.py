class ListComparator:
    def compare(self, list_a, list_b):
        if len(list_a) != len(list_b):
            return False
        for item_a, item_b in zip(list_a, list_b):
            if item_a != item_b:
                return False
        return True
if __name__ == '__main__':
    comparator = ListComparator()
    list1 = [1, 2, 3]
    list2 = [1, 2, 3]
    list3 = [1, 2, 4]
    list4 = [1, 2]
    list5 = []
    list6 = []
    list7 = [1, 2, 3, 4]
    list8 = [1, 2, 3]
    print(f"Comparing {list1} and {list2}: {comparator.compare(list1, list2)}")
    print(f"Comparing {list1} and {list3}: {comparator.compare(list1, list3)}")
    print(f"Comparing {list4} and {list8}: {comparator.compare(list4, list8)}")
    print(f"Comparing {list5} and {list6}: {comparator.compare(list5, list6)}")
    print(f"Comparing {list7} and {list8}: {comparator.compare(list7, list8)}")