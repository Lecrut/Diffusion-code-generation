import random

def generate_random_list(length):
    return [random.randint(-1000, 1000) for _ in range(length)]

def find_minimum(data):
    if not data:
        raise ValueError("Input list cannot be empty")
    
    minimum = data[0]
    for item in data[1:]:
        if item < minimum:
            minimum = item
    return minimum

if __name__ == '__main__':
    sample_data = generate_random_list(10)
    print("Sample Data:", sample_data)
    print("Minimum Value:", find_minimum(sample_data))