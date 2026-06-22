def _validate_pair(a, b):
    try:
        if a > b:
            return True
        if b > a:
            return True
        return True
    except TypeError:
        raise TypeError("Arguments must be comparable")

def sort_pair(a, b):
    _validate_pair(a, b)
    if a <= b:
        return (a, b)
    return (b, a)

class PairSorter:
    def __init__(self, first, second):
        self.first = first
        self.second = second

    def get_sorted(self):
        return sort_pair(self.first, self.second)

if __name__ == '__main__':
    print(sort_pair(15, 7))
    print(sort_pair(20.5, 20.5))
    print(sort_pair(-3, -10))
    instance = PairSorter(100, 50)
    print(instance.get_sorted())
    print(sort_pair(10, 20))