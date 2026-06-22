import random

def find_max_value(data):
    if not data:
        return None
    max_value = data[0]
    for value in data[1:]:
        if value > max_value:
            max_value = value
    return max_value

if __name__ == '__main__':
    sample_data = [random.randint(1, 100) for _ in range(10)]
    print("Original list:", sample_data)
    max_val = find_max_value(sample_data)
    print("Maximum value:", max_val)