class ListComparator:
    @staticmethod
    def compare_elements(element1, element2):
        if element1 > element2:
            print(f"List 1: {element1} is greater than List 2: {element2}")

    @classmethod
    def compare_lists(cls, list1, list2):
        min_length = min(len(list1), len(list2))
        for index in range(min_length):
            cls.compare_elements(list1[index], list2[index])

if __name__ == '__main__':
    list_a = [10, 20, 30, 40]
    list_b = [10, 25, 30, 50]
    ListComparator.compare_lists(list_a, list_b)