class ListDifference:

    @staticmethod
    def find_unique_elements(list_a, list_b):
        unique_in_list_a = []
        for item in list_a:
            if item not in list_b and item not in unique_in_list_a:
                unique_in_list_a.append(item)
        return unique_in_list_a
if __name__ == '__main__':
    list1 = [1, 2, 3, 4]
    list2 = [3, 4, 5, 6]
    result = ListDifference.find_unique_elements(list1, list2)
    print(result)