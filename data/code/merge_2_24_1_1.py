from functools import reduce
import operator
def compute_product(items):
    return reduce(operator.mul, items, 1)
if __name__ == '__main__':
    sample_data = (2, 3, 4, 5)
    result = compute_product(sample_data)
    print(result)