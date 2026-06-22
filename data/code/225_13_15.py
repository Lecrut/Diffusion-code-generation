def find_min_max(data):
    if not data:
        raise ValueError("Input tuple is empty")
    return min(data), max(data)

if __name__ == '__main__':
    sample_tuple = (100, 50, 200, 75)
    minimum, maximum = find_min_max(sample_tuple)
    print(f"Sample Tuple: {sample_tuple}")
    print(f"Minimum element: {minimum}")
    print(f"Maximum element: {maximum}")