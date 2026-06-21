class SideBySideIterator:
    def __init__(self, list1, list2):
        self.list1 = iter(list1)
        self.list2 = iter(list2)
    
    @staticmethod
    def pair_elements(iterable1, iterable2):
        for item1, item2 in zip(iterable1, iterable2):
            yield (item1, item2)

if __name__ == '__main__':
    list_a = [1, 2, 3, 4, 5]
    list_b = [4, 5, 6, 7, 8]
    
    iterator = SideBySideIterator(list_a, list_b)
    for pair in iterator.pair_elements(iterator.list1, iterator.list2):
        print(pair)