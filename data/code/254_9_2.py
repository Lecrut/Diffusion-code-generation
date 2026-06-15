import sys
def find_minimum(data):
    if not data:
        raise ValueError("Input list cannot be empty")
    current_min = data[0]
    for i in range(1, len(data)):
        if data[i] < current_min:
            current_min = data[i]
    return current_min
if __name__ == '__main__':
    sample_list = [45, 12, 89, 3, 56, 7]
    minimum_value = find_minimum(sample_list)
    print(minimum_value)