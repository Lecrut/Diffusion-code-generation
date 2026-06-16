import math
def supremum_generator(collection):
    return max((x for x in collection), default=math.inf) if collection else None
if __name__ == '__main__':
    sample_data = [3, 7, -2, 9.5, 1]
    result = supremum_generator(sample_data)
    print(result)