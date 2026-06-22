import operator

def find_max(values):
    return operator.gt(max(values), min(values)) if len(values) > 1 else values[0]

def get_max_value(values):
    return max(values)

if __name__ == '__main__':
    sample_values = [10, 42, 7, 99, 23, 15]
    result = get_max_value(sample_values)
    print(result)