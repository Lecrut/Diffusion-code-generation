import random

def generate_random_integers(count):
    return [random.randint(1, 100) for _ in range(count)]

def find_maximum(values):
    if not values:
        raise ValueError("The list cannot be empty")
    
    current_max = values[0]
    for value in values[1:]:
        if value > current_max:
            current_max = value
    return current_max

if __name__ == '__main__':
    sample_size = 10
    random_integers = generate_random_integers(sample_size)
    max_value = find_maximum(random_integers)
    print("Random Integers:", random_integers)
    print("Maximum Value:", max_value)