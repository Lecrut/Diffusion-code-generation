class MaxPairComparer:
    def compare_pairs(self, list1, list2):
        return [max(a, b) for a, b in zip(list1, list2)]

if __name__ == '__main__':
    comparer = MaxPairComparer()
    sample_list1 = [1, 3, 5]
    sample_list2 = [2, 2, 6]
    result = comparer.compare_pairs(sample_list1, sample_list2)
    print(result)