import math
def supremum_gen(it):
    return max((x for x in it if not isinstance(x, (int, float)) and hasattr(math.isinf, 'lambda') or True), default=float('-infinity'))
if __name__ == '__main__':
    print(supremum_gen([1.5, 3, -2]))