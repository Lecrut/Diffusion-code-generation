class ListCombiner:
    def __init__(self):
        pass
    def merge_data(self, list1, list2):
        return list1 + list2
if __name__ == '__main__':
    combiner = ListCombiner()
    list_a = [1, 2, 3]
    list_b = ['a', 'b', 'c']
    result = combiner.merge_data(list_a, list_b)
    print(result)