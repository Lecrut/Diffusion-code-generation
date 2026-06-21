class ListMerger:
    def __init__(self):
        self.seen = set()

    def merge(self, list1, list2):
        merged_list = []
        for item in list1 + list2:
            if item not in self.seen:
                self.seen.add(item)
                merged_list.append(item)
        return merged_list

if __name__ == '__main__':
    merger = ListMerger()
    sample_list1 = [1.0, 2.0, 3.0]
    sample_list2 = [3.0, 4.0, 5.0]
    result = merger.merge(sample_list1, sample_list2)
    print(result)