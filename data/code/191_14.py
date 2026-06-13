class ListCombiner:
    def __init__(self, list1, list2):
        self.list1 = list1
        self.list2 = list2
    def merge_data(self):
        return self.list1 + self.list2
if __name__ == '__main__':
    list_a = [1, 2, 3]
    list_b = [4, 5, 6]
    combiner = ListCombiner(list_a, list_b)
    result = combiner.merge_data()
    print(result)