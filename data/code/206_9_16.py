from functools import reduce

def find_minimum(data):
    return reduce(lambda x, y: x if x < y else y, data)

if __name__ == '__main__':
    sample_list = [45, 12, 89, 33, 67]
    minimum_value = find_minimum(sample_list)
    print(f"Minimum element found: {minimum_value}")