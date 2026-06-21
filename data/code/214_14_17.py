MIN_VALUE = float('inf')

def find_min_value(data):
    min_val = MIN_VALUE
    for num in data:
        if num < min_val:
            min_val = num
    return min_val

if __name__ == '__main__':
    sample_data = [5, 3, 9, 1, 10]
    print(find_min_value(sample_data))