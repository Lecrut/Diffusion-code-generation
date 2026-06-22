import operator

def find_maximum(*numbers):
    return max(numbers, key=operator.itemgetter(0)) if numbers else None

if __name__ == '__main__':
    sample_values = (42, 15, 98, 3, 56, 27, 81, 10, 64, 39)
    result = find_maximum(*sample_values)
    print(result)