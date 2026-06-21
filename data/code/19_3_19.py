import random
import sys

class RandomTupleSelector:
    def __init__(self, source):
        self.source = source

    def get_random(self):
        if not self.source:
            return None
        index = random.randrange(len(self.source))
        return self.source[index]

    def get_all_items(self):
        return list(self.source)

if __name__ == '__main__':
    data = (1, 2, 3, 4, 5)
    empty_data = ()
    selector1 = RandomTupleSelector(data)
    selector2 = RandomTupleSelector(empty_data)
    val1 = selector1.get_random()
    print(val1)
    val2 = selector2.get_random()
    print(val2)
    items = selector1.get_all_items()
    print(items)