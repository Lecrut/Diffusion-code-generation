import random

def find_minimum(data):
    if not data:
        raise ValueError("Input list cannot be empty")
    minimum = data[0]
    for element in data[1:]:
        if element < minimum:
            minimum = element
    return minimum

if __name__ == '__main__':
    sample_data = [random.randint(-1000, 1000) for _ in range(1_000_000)]
    print(f"Minimum of sample data: {find_minimum(sample_data)}")