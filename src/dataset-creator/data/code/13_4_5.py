import math
def supremum(iterable):
    return max((x for x in iterable), default=math.inf) if iterable else None
if __name__ == '__main__':
    data = [3, 7, -2, 9, 0]
    result = supremum(data)
    print(result)