import math
def supremum_gen(collection):
    return max((x for x in collection), default=math.inf) if collection else float('-inf')
if __name__ == '__main__':
    print(supremum_gen([1, 5, 3.2, -10]))