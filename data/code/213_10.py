def analyze_list(data):
    total_sum = sum(data)
    count = len(data)
    average = total_sum / count if count > 0 else 0
    range_val = max(data) - min(data) if count > 0 else 0
    return total_sum, average, range_val
if __name__ == '__main__':
    sample_list = [10, 25, 32, 8, 45]
    total, avg, r = analyze_list(sample_list)
    print(f"List: {sample_list}")
    print(f"Sum: {total}")
    print(f"Average: {avg}")
    print(f"Range: {r}")