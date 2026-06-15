import math
def find_max_efficiently(data):
    if not data:
        raise ValueError("Input list cannot be empty")
    max_value = data[0]
    for i in range(1, len(data)):
        if data[i] > max_value:
            max_value = data[i]
    return max_value
if __name__ == '__main__':
    large_list = [3.1415926535, -0.5, 100.75, -3.1415926535, 99.999999999]
    try:
        maximum = find_max_efficiently(large_list)
        print(maximum)
    except ValueError as e:
        print(e)