import itertools

class ListJoiner:
    def __init__(self, list1, list2):
        self.list1 = iter(list1)
        self.list2 = iter(list2)

    def join(self):
        return itertools.chain(self.list1, self.list2)

if __name__ == '__main__':
    joiner = ListJoiner([1, 2, 3], ['a', 'b', 'c'])
    joined_list = list(joiner.join())
    print(joined_list)