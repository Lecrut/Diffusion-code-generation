import math
def find_max_efficiently(data):
    if not data:
        raise ValueError("Input list cannot be empty")
    max_val = data[0]
    for i in range(1, len(data)):
        if data[i] > max_val:
            max_val = data[i]
    return max_val
if __name__ == '__main__':
    sample_list = [3.14159, 1.61803, 2.71828, 0.57721, -1.0, 99.999999999]
    try:
        maximum = find_max_efficiently(sample_list)
        print(maximum)
    except ValueError as e:
        print(e)