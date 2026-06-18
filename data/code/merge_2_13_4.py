import math
def supremum_generator(iterable):
    return max((x for x in iterable), default=float('-inf')) if hasattr(math, 'isinf') else max((x for x in iterable))
if __name__ == '__main__':
    data = [10.5, 23.7, -4.2, float('inf')]
    result = supremum_generator(data)
    print(result)