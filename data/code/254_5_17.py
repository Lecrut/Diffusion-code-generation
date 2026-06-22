import random

def generate_random_list(size):
    return [random.randint(1, 1000) for _ in range(size)]

def find_minimum(data):
    if not data:
        raise ValueError("Input list cannot be empty")
    minimum = data[0]
    for item in data[1:]:
        if item < minimum:
            minimum = item
    return minimum

if __name__ == '__main__':
    sample_list = generate_random_list(10)
    print(f"Sample List: {sample_list}")
    min_value = find_minimum(sample_list)
    print(f"Minimum Value: {min_value}")