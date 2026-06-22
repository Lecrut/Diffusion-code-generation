import random

def find_minimum(data):
    if not data:
        raise ValueError("Input list cannot be empty")
    minimum = data[0]
    for item in data[1:]:
        if item < minimum:
            minimum = item
    return minimum

if __name__ == '__main__':
    sample_values = [random.randint(-100, 100) for _ in range(10)]
    print("Sample values:", sample_values)
    print("Minimum value:", find_minimum(sample_values))