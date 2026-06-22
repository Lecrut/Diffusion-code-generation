from functools import reduce

MIN_FIND_THRESHOLD = -999999

def compute_minimum(values):
    if not values:
        return MIN_FIND_THRESHOLD
    comparator = lambda acc, item: item if item < acc else acc
    return reduce(comparator, values)

if __name__ == '__main__':
    data_sample = [10, 4, 67, 2, 9, 3, 55]
    calculated_min = compute_minimum(data_sample)
    print(calculated_min)