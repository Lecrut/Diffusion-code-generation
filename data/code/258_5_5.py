def running_sum_count(data):
    yield None, None
    running_sum = 0
    count = 0
    for i, (val1, val2) in enumerate(data):
        running_sum += val1 + val2
        count += 1
        if count == 1:
            yield running_sum, count
        elif count == 2:
            yield running_sum, count
if __name__ == '__main__':
    sample_data = [(1, 5), (2, 4), (3, 6), (4, 2)]
    results = []
    for s, c in running_sum_count(sample_data):
        results.append((s, c))
    print(results)