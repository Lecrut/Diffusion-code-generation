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
    large_list = [random.randint(0, 1000000) for _ in range(1000000)]
    print(f"List size: {len(large_list)}")
    minimum_element = find_minimum(large_list)
    print(f"Minimum element found: {minimum_element}")