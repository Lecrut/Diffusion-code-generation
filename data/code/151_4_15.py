class ListCombiner:
    def zip_lists(self, list1, list2):
        try:
            return list(zip(list1, list2))
        except TypeError as e:
            return [f"Error: {e}"]

if __name__ == '__main__':
    combiner = ListCombiner()
    list_a = [1, 2, 3]
    list_b = ['a', 'b', 'c']
    result1 = combiner.zip_lists(list_a, list_b)
    print(f"Zipped {list_a} and {list_b}: {result1}")