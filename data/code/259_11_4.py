def find_min_max(data):
    return min(data), max(data)
if __name__ == '__main__':
    sample_list = [3, 1, 4, 1, 5, 9, 2, 8, 7, 6]
    minimum, maximum = find_min_max(sample_list)
    print(f"Minimum: {minimum}, Maximum: {maximum}")