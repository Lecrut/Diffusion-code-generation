class MaxPairFinder:
    @staticmethod
    def find_max_pairs(list1, list2):
        return [max(a, b) for a, b in zip(list1, list2)]

if __name__ == '__main__':
    sample_list1 = [1, 3, 5]
    sample_list2 = [2, 2, 6]
    result = MaxPairFinder.find_max_pairs(sample_list1, sample_list2)
    print(result)