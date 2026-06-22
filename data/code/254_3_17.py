import random

def find_min_value(data):
    min_val = float('inf')
    for value in data:
        if value < min_val:
            min_val = value
    return min_val

if __name__ == '__main__':
    sample_data = [random.randint(1, 1000000) for _ in range(1000000)]
    print(find_min_value(sample_data))