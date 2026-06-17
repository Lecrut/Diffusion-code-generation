import math
def find_range(data):
    if not data:
        return None
    min_val = data[0]
    max_val = data[0]
    for x in data:
        if x < min_val:
            min_val = x
        if x > max_val:
            max_val = x
    return max_val - min_val
if __name__ == '__main__':
    sample_data = [3.14159, 1.61803, 2.71828, 0.57721, 4.0, -1.0, 100.0, -50.5]
    range_result = find_range(sample_data)
    print(range_result)