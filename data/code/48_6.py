import operator

def find_max_integers(numbers):
    if not numbers:
        return None
    return max(numbers, key=operator.itemgetter(0)) if isinstance(numbers[0], tuple) else max(numbers)

if __name__ == '__main__':
    sample_values = [10, 45, 3, 99, 22, 5, 101, 7]
    result = find_max_integers(sample_values)
    print(result)