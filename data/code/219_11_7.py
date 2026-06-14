import math
def find_max_efficient(data):
    if not data:
        raise ValueError("Input list cannot be empty")
    max_val = data[0]
    for i in range(1, len(data)):
        if data[i] > max_val:
            max_val = data[i]
    return max_val
if __name__ == '__main__':
    large_list = [3.1415926535, 1.6180339887, -0.5, 100.0, 99.99999999999999, -100.0]
    try:
        maximum = find_max_efficient(large_list)
        print(maximum)
    except ValueError as e:
        print(e)