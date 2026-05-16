def calculate_stats(data):
    if not data:
        return None, None, None
    running_total = 0
    product = 1
    min_val = data[0]
    max_val = data[0]
    for x in data:
        running_total += x
        product *= x
        if x < min_val:
            min_val = x
        if x > max_val:
            max_val = x
    return running_total, product, max_val - min_val
if __name__ == '__main__':
    sample_list = [1, 5, 2, 8, 3]
    total, prod, range_val = calculate_stats(sample_list)
    print(f"Running Total: {total}")
    print(f"Product: {prod}")
    print(f"Range (Max - Min): {range_val}")