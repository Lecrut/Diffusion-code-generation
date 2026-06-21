import itertools

class ListJoiner:
    def __init__(self, list1, list2):
        self.list1 = list1
        self.list2 = list2
    
    def join_lists(self):
        return list(itertools.chain(self.list1, self.list2))

if __name__ == '__main__':
    joiner = ListJoiner([1, 2, 3], ['a', 'b', 'c'])
    result = joiner.join_lists()
    print(result)