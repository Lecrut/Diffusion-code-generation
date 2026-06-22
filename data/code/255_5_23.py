import random

def generate_random_list(size):
    return [random.randint(1, 100) for _ in range(size)]

def find_max_value(data):
    if not data:
        return None
    max_value = data[0]
    for value in data[1:]:
        if value > max_value:
            max_value = value
    return max_value

if __name__ == '__main__':
    sample_list = generate_random_list(10)
    print("Random List:", sample_list)
    max_val = find_max_value(sample_list)
    print("Maximum Value:", max_val)