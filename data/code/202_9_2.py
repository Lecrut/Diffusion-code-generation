import random
def find_maximum(data):
    if not data:
        raise ValueError("Input list cannot be empty")
    max_value = data[0]
    for num in data[1:]:
        if num > max_value:
            max_value = num
    return max_value
if __name__ == '__main__':
    random.seed(42)
    large_list = [random.randint(1, 1000000) for _ in range(1000000)]
    max_val = find_maximum(large_list)
    print(max_val)