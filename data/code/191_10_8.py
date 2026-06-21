class ListCombiner:
    def __init__(self, list1, list2):
        self.list1 = list1.copy()
        self.list2 = list2

    def combine(self):
        self.list1.extend(self.list2)
        return self.list1

if __name__ == '__main__':
    combiner = ListCombiner([1, 2, 3], [4, 5, 6])
    combined_list = combiner.combine()
    print(combined_list)