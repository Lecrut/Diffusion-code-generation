import random
def find_max_optimized(data):
    if not data:
        raise ValueError("Input list cannot be empty")
    max_val = data[0]
    for i in range(1, len(data)):
        if data[i] > max_val:
            max_val = data[i]
    return max_val
if __name__ == '__main__':
    random.seed(42)
    large_list = [random.uniform(-1000.5, 1000.5) for _ in range(1000000)]
    print(find_max_optimized(large_list))