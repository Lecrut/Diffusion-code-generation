class ElementWiseMax:
    @staticmethod
    def max_pairs(list1, list2):
        return [max(a, b) for a, b in zip(list1, list2)]

if __name__ == '__main__':
    sample_list1 = [4, 6, 8]
    sample_list2 = [3, 9, 7]
    result = ElementWiseMax.max_pairs(sample_list1, sample_list2)
    print(result)