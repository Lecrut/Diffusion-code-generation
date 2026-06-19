class IndexFinder:
    def __init__(self, item_indices):
        self.item_indices = item_indices

    def find_final_item_index(self):
        if not self.item_indices:
            return -1
        return len(self.item_indices) - 1

if __name__ == '__main__':
    list1 = [1, 5, 2, 8, 3]
    finder1 = IndexFinder(list1)
    result1 = finder1.find_final_item_index()
    print(result1)

    list2 = [100]
    finder2 = IndexFinder(list2)
    result2 = finder2.find_final_item_index()
    print(result2)

    list3 = []
    finder3 = IndexFinder(list3)
    result3 = finder3.find_final_item_index()
    print(result3)

    list4 = [42]
    finder4 = IndexFinder(list4)
    result4 = finder4.find_final_item_index()
    print(result4)