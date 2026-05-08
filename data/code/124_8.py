def calculate_running_stats(data):
    if not data:
        return None, None, None
    running_total = 0
    running_product = 1
    min_val = data[0]
    max_val = data[0]
    results = []
    for i, x in enumerate(data):
        running_total += x
        running_product *= x
        if x < min_val:
            min_val = x
        if x > max_val:
            max_val = x
        range_val = max_val - min_val
        results.append((running_total, running_product, range_val))
    return results
if __name__ == '__main__':
    sample_data = [2, 5, 1, 8, 3]
    stats = calculate_running_stats(sample_data)
    print(stats)