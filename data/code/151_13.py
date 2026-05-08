class ListCombiner:
    def merge(self, list1, list2):
        combined_set = set(list1)
        combined_set.update(list2)
        sorted_list = sorted(list(combined_set))
        return sorted_list
if __name__ == '__main__':
    combiner = ListCombiner()
    list_a = [1, 5, 2, 8, 5]
    list_b = [8, 3, 1, 9, 2]
    result = combiner.merge(list_a, list_b)
    print(result)