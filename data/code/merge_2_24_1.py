from functools import reduce
import operator
def dynamic_product(items):
    return reduce(operator.mul, items, 1)
if __name__ == '__main__':
    sample_tuple = (2, 3, 4, 5)
    result = dynamic_product(sample_tuple)
    print(result)