class ListMerger:
    def __init__(self):
        self.result = []

    def merge(self, list_a, list_b):
        self.result.extend(list_a)
        self.result.extend(list_b)

if __name__ == '__main__':
    merger = ListMerger()
    list1 = [1, 2, 3]
    list2 = [4, 5, 6]
    merger.merge(list1, list2)
    print("Merged List:", merger.result)