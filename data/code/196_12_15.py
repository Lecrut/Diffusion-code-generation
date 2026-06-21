class StringCombiner:
    LIST_A = ["apple", "banana"]
    LIST_B = ["cherry", "date"]

    @staticmethod
    def combine_lists(list1, list2):
        return list1 + list2

if __name__ == '__main__':
    combiner = StringCombiner()
    result = combiner.combine_lists(StringCombiner.LIST_A, StringCombiner.LIST_B)
    print(result)