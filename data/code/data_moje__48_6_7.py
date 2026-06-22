import operator

def find_max(*numbers):
    return max(numbers, key=operator.itemgetter(0)) if numbers else None

def find_max_operator(numbers):
    return max(numbers, key=lambda x: x)

def get_maximum(iterable):
    return max(iterable)

if __name__ == '__main__':
    sample_values = [1, 5, 3, 9, 2, 8, 4]
    result = get_maximum(sample_values)
    print(result)