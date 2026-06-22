import operator

def find_max_integers(numbers):
    if not numbers:
        return None
    max_val = numbers[0]
    for num in numbers[1:]:
        max_val = operator.max_(max_val, num)
    return max_val

if __name__ == '__main__':
    sample_values = [34, 78, 12, 99, 45, 2, 88]
    result = find_max_integers(sample_values)
    print(result)