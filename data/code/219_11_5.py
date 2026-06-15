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
    large_list = [3.141592653589793, -10.5, 99.99999999999999, 0.0, 42.0, 1.2e308, -5.0]
    try:
        maximum = find_max_efficiently(large_list)
        print(maximum)
    except ValueError as e:
        print(f"Error: {e}")