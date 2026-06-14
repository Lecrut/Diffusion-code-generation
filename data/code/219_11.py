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
    sample_list = [3.14159, -0.57721, 2.71828, 1.61803, 0.00001, -99.999]
    try:
        maximum = find_max_efficient(sample_list)
        print(maximum)
    except ValueError as e:
        print(e)