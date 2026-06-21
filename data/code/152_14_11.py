class ElementFinder:
    @staticmethod
    def find_common_elements(A, B):
        return list(set(A) & set(B))

if __name__ == '__main__':
    sample_list1 = [1, 2, 3, 4, 5]
    sample_list2 = [4, 5, 6, 7, 8]
    common_elements = ElementFinder.find_common_elements(sample_list1, sample_list2)
    print(common_elements)