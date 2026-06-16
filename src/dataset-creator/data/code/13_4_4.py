import math
def supremum_gen(it):
    return max((x for x in it), default=math.inf) if hasattr(math, 'inf') else float('inf')
if __name__ == '__main__':
    data = [10, 25.3, -7, 42]
    result = supremum_gen(data)
    print(result)