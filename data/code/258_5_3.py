def running_sum_count(data):
    yield None, None
    current_sum = 0
    current_count = 0
    for i, (a, b) in enumerate(data):
        current_sum += a + b
        current_count += 1
        if current_count == 1:
            yield current_sum, current_count
        elif current_count == 2:
            yield current_sum, current_count
if __name__ == '__main__':
    sample_data = [(1, 5), (2, 4), (3, 6), (4, 2)]
    results = list(running_sum_count(sample_data))
    for sum_val, count in results:
        print(f"Running Sum: {sum_val}, Count: {count}")