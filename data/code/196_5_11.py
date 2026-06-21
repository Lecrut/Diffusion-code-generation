import itertools

class ListJoiner:
    @staticmethod
    def join_lists(list1, list2):
        return list(itertools.chain(list1, list2))

if __name__ == '__main__':
    list_a = [1, 2, 3]
    list_b = ['a', 'b', 'c']
    joined_list = ListJoiner.join_lists(list_a, list_b)
    print(joined_list)