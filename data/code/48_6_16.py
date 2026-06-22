import operator

def find_maximum(numbers):
    if not numbers:
        return None
    return reduce(operator.max, numbers)

def reduce(op, items):
    result = items[0]
    for item in items[1:]:
        result = op(result, item)
    return result

if __name__ == '__main__':
    sample_values = [10, 25, 3, 47, 12, 8, 99, 2]
    max_value = find_maximum(sample_values)
    print(max_value)