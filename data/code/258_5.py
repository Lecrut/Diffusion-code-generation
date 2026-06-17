def running_sum_count(data):
    yield None, None
    current_sum = 0
    current_count = 0
    for i, (value1, value2) in enumerate(data):
        if i == 0:
            current_sum = value1 + value2
            current_count = 2
        else:
            current_sum += value1 + value2
            current_count += 2
        yield current_sum, current_count
if __name__ == '__main__':
    sample_data = [(10, 5), (20, 8), (30, 12)]
    results = running_sum_count(sample_data)
    print("Index | Running Sum | Count")
    print("--------------------------")
    for i, (s, c) in enumerate(results):
        if s is not None:
            average = s / c
            print(f"{i}    | {s}         | {c} (Average: {average:.2f})")