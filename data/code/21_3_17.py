from functools import reduce
import operator

def determine_maximum(x, y, z):
    candidates = [x, y, z]
    largest = reduce(operator.gt, candidates, candidates[0])
    return largest

if __name__ == '__main__':
    val_a = 89.12
    val_b = 72.45
    val_c = 94.87
    maximum_value = determine_maximum(val_a, val_b, val_c)
    print(maximum_value)