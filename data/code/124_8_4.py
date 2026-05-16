def calculate_running_stats(data):
    if not data:
        return [], [], []
    running_total = 0
    running_product = 1
    min_val = data[0]
    max_val = data[0]
    results = []
    for i, x in enumerate(data):
        running_total += x
        running_product *= x
        if i > 0:
            running_range = max_val - min_val
        else:
            running_range = 0
        min_val = min(min_val, x)
        max_val = max(max_val, x)
        results.append((running_total, running_product, max_val - min_val))
    return results
if __name__ == '__main__':
    sample_data = [1, 2, 3, 4, 5]
    output = calculate_running_stats(sample_data)
    print(output)