def find_min_max(data):
    return min(data), max(data)
if __name__ == '__main__':
    sample_list = [10, 4, 25, 8, 30, 15]
    minimum, maximum = find_min_max(sample_list)
    print(f"Minimum: {minimum}")
    print(f"Maximum: {maximum}")