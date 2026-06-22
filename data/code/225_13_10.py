sample_tuple = (100, 50, 200, 75)

def find_min_max(data):
    return min(data), max(data)

if __name__ == '__main__':
    minimum, maximum = find_min_max(sample_tuple)
    print(f"Sample Tuple: {sample_tuple}")
    print(f"Minimum element: {minimum}")
    print(f"Maximum element: {maximum}")