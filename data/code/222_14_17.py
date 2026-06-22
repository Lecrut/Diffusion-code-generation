def find_minimum(data):
    if not data:
        raise ValueError("Input list cannot be empty")
    return min(data)

if __name__ == '__main__':
    large_list = [45, 12, 89, 3, 67, 22, 90, -5, 101, 33]
    minimum = find_minimum(large_list)
    print(minimum)