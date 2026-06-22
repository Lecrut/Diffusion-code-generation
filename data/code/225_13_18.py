def compute_min_max(data):
    return min(data), max(data)

if __name__ == '__main__':
    sample_tuple = (3, 7, 2, 5, 9)
    minimum, maximum = compute_min_max(sample_tuple)
    print(f"Sample Tuple: {sample_tuple}")
    print(f"Minimum element: {minimum}")
    print(f"Maximum element: {maximum}")