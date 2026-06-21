MIN_VALUE = float('inf')

def find_min_value(data):
    if not data:
        return MIN_VALUE
    min_val = data[0]
    for value in data[1:]:
        if value < min_val:
            min_val = value
    return min_val

if __name__ == '__main__':
    sample_data = [5, 3, 9, 1, 10]
    print(find_min_value(sample_data))