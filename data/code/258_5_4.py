def running_sum_count(data):
    yield None, None
    current_sum = 0
    current_count = 0
    for i, (value1, value2) in enumerate(data):
        current_sum += value1 + value2
        current_count += 1
        if current_count == 1:
            yield current_sum, current_count
        elif current_count == 2:
            yield current_sum, current_count
if __name__ == '__main__':
    sample_data = [(10, 5), (20, 8), (30, 12), (40, 16)]
    results = []
    for sum_val, count in running_sum_count(sample_data):
        results.append((sum_val, count))
    print(results)