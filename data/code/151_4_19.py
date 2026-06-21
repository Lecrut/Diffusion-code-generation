class TupleCombiner:
    @staticmethod
    def combine(list1, list2):
        return list(zip(list1, list2))

if __name__ == '__main__':
    combiner = TupleCombiner()
    list_a = [1, 2, 3]
    list_b = ['a', 'b', 'c']
    result = combiner.combine(list_a, list_b)
    print(f"Combined tuples of {list_a} and {list_b}: {result}")