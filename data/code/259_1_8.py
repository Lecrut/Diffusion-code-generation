MIN_VALUE = float('-inf')
MAX_VALUE = float('inf')

def find_min_max(data):
    min_val = MIN_VALUE
    max_val = MAX_VALUE
    for num in data:
        if num < min_val:
            min_val = num
        if num > max_val:
            max_val = num
    return min_val, max_val

if __name__ == '__main__':
    sample_list = [3, 1, 4, 1, 5, 9, 2, 6]
    result = find_min_max(sample_list)
    print(result)