import sys
def find_minimum(data):
    if not data:
        raise ValueError("Input list cannot be empty")
    current_minimum = data[0]
    for i in range(1, len(data)):
        if data[i] < current_minimum:
            current_minimum = data[i]
    return current_minimum
if __name__ == '__main__':
    sample_list = [45, 12, 89, 3, 56, 77]
    minimum_value = find_minimum(sample_list)
    print(minimum_value)