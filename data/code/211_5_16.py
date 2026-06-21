class PairwiseIterator:
    def __init__(self, list1, list2):
        self.list1 = iter(list1)
        self.list2 = iter(list2)
    
    def __iter__(self):
        return self
    
    def __next__(self):
        try:
            item1 = next(self.list1)
            item2 = next(self.list2)
            return (item1, item2)
        except StopIteration:
            raise StopIteration

if __name__ == '__main__':
    iterator = PairwiseIterator([1, 2, 3], [4, 5])
    for pair in iterator:
        print(pair)