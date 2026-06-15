def analyze_list(numbers):
    if not numbers:
        return None
    smallest = min(numbers)
    largest = max(numbers)
    distinct_count = len(set(numbers))
    return (smallest, largest, distinct_count)
if __name__ == '__main__':
    sample_list = [1, 5, 2, 8, 5, 1, 9, 2]
    result = analyze_list(sample_list)
    print(result)