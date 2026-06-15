def analyze_list(numbers):
    if not numbers:
        return None, None, None
    total_sum = sum(numbers)
    count = len(numbers)
    average = total_sum / count
    minimum = min(numbers)
    maximum = max(numbers)
    data_range = maximum - minimum
    return total_sum, average, data_range
if __name__ == '__main__':
    sample_list = [10, 25, 32, 8, 41, 15]
    total, avg, rng = analyze_list(sample_list)
    print(f"List: {sample_list}")
    print(f"Sum: {total}")
    print(f"Average: {avg}")
    print(f"Range: {rng}")