def find_min_max(data):
    return min(data), max(data)

if __name__ == '__main__':
    sample_tuple = (15, 3, 8, 22, 1, 45, 9)
    minimum, maximum = find_min_max(sample_tuple)
    print(f"Sample Tuple: {sample_tuple}")
    print(f"Minimum element: {minimum}")
    print(f"Maximum element: {maximum}")