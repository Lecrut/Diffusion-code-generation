class FirstLastIterator:
    def __init__(self, iterable):
        self.iterable = iter(iterable)
    
    @staticmethod
    def _get_first_and_last(iterator):
        try:
            first = next(iterator)
        except StopIteration:
            return None, None
        
        last = None
        for item in iterator:
            last = item
        
        return first, last
    
    def __iter__(self):
        first, last = self._get_first_and_last(self.iterable)
        if first is not None:
            yield first
        if last is not None:
            yield last

if __name__ == '__main__':
    data1 = [1, 2, 3, 4, 5]
    print(list(FirstLastIterator(data1)))
    
    data2 = [10]
    print(list(FirstLastIterator(data2)))
    
    data3 = [100]
    print(list(FirstLastIterator(data3)))