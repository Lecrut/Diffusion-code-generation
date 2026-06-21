class ListMerger:
    def __init__(self, list1, list2):
        self.list1 = list1
        self.list2 = list2
    
    def merge_lists(self):
        return [item for sublist in (self.list1, self.list2) for item in sublist]

if __name__ == '__main__':
    sample_list_a = [1, 2, 3]
    sample_list_b = ['a', 'b', 'c']
    merger = ListMerger(sample_list_a, sample_list_b)
    result = merger.merge_lists()
    print(result)