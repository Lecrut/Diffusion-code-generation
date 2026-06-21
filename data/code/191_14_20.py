class ListMerger:
    def __init__(self, list1, list2):
        self.list1 = list1
        self.list2 = list2

    def merge_lists(self):
        return [item for sublist in (self.list1, self.list2) for item in sublist]

if __name__ == '__main__':
    sample_list1 = [1, 2, 3]
    sample_list2 = ['a', 'b', 'c']
    merger = ListMerger(sample_list1, sample_list2)
    result = merger.merge_lists()
    print(result)