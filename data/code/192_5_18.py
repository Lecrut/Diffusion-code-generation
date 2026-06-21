class ElementFinder:
    @staticmethod
    def create_set_from_list(input_list):
        return set(input_list)
    
    @staticmethod
    def find_common_elements(set1, set2):
        return set1.intersection(set2)

if __name__ == '__main__':
    list_a = [1, 2, 3, 4, 5, 5]
    list_b = [4, 5, 6, 7, 8, 4]
    finder = ElementFinder()
    set_a = finder.create_set_from_list(list_a)
    set_b = finder.create_set_from_list(list_b)
    common = finder.find_common_elements(set_a, set_b)
    print(common)