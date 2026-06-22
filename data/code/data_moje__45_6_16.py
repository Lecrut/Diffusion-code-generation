from functools import reduce

def find_minimum(values):
    return reduce(lambda x, y: x if x < y else y, values)

if __name__ == '__main__':
    sample_data = [12, 5, 9, 23, 4, 67, 3]
    result = find_minimum(sample_data)
    print(result)