class ElementFinder:
    @staticmethod
    def find_common_elements(A, B):
        set_A = set(A)
        return [item for item in B if item in set_A]

if __name__ == '__main__':
    list_a = [1, 2, 3, 4, 5]
    list_b = [4, 5, 6, 7, 8]
    common = ElementFinder.find_common_elements(list_a, list_b)
    print(common)