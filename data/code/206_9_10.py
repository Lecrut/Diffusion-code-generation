from functools import reduce

MIN_VALUE = float('inf')

def find_minimum(data):
    if not data:
        raise ValueError("Input list cannot be empty")
    
    return reduce(lambda x, y: x if x < y else y, data, MIN_VALUE)

if __name__ == '__main__':
    large_list = [random.randint(0, 1000000) for _ in range(1000000)]
    minimum_value = find_minimum(large_list)
    print(f"Minimum element found: {minimum_value}")