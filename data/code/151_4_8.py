class ListCombiner:
    def merge(self, list1, list2):
        if not isinstance(list1, list) or not isinstance(list2, list):
            raise TypeError("Both inputs must be lists.")
        return list(zip(list1, list2))

if __name__ == '__main__':
    combiner = ListCombiner()
    list_a = [1, 2, 3]
    list_b = ['a', 'b', 'c']
    result = combiner.merge(list_a, list_b)
    print(f"Merged pairs of {list_a} and {list_b}: {result}")