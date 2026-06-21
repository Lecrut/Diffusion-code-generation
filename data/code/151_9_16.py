class SetMerger:
    @staticmethod
    def merge(list1, list2):
        return set().union(*list1, *list2)

if __name__ == '__main__':
    sample_list1 = [{1, 2}, {3, 4}]
    sample_list2 = [{4, 5}, {6, 7}]
    merger = SetMerger()
    result = merger.merge(sample_list1, sample_list2)
    print(result)