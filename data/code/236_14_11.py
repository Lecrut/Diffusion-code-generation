from itertools import chain

class ListRepeater:
    def __init__(self, original):
        self.original = original
    
    def repeat(self, n):
        return list(chain.from_iterable([self.original] * n))

if __name__ == '__main__':
    repeater = ListRepeater([1, 2, 3])
    result = repeater.repeat(3)
    print(result)