def analyze_list(data):
    if not data:
        return None, None, None
    total_sum = sum(data)
    count = len(data)
    average = total_sum / count
    minimum = min(data)
    maximum = max(data)
    data_range = maximum - minimum
    return total_sum, average, data_range
if __name__ == '__main__':
    sample_list = [10, 25, 32, 8, 45]
    total, avg, rng = analyze_list(sample_list)
    print(f"List: {sample_list}")
    print(f"Sum: {total}")
    print(f"Average: {avg}")
    print(f"Range: {rng}")