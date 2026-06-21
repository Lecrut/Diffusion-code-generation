class ListCombiner:
    @staticmethod
    def concatenate(list1, list2):
        return list1 + list2

if __name__ == '__main__':
    result = ListCombiner.concatenate([1, 2], [3, 4])
    print(result)