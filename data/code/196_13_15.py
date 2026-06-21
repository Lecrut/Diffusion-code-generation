class ListMerger:
    def __init__(self):
        self.list1 = [1, 2, 3]
        self.list2 = [4, 5, 6]

    def merge_lists(self):
        self.list1 += self.list2

if __name__ == '__main__':
    merger = ListMerger()
    merger.merge_lists()
    print("Merged List:", merger.list1)