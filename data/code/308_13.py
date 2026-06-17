def analyze_sequence(numbers):
    total_count = len(numbers)
    total_sum = sum(numbers)
    return {
        "count": total_count,
        "sum": total_sum
    }
if __name__ == '__main__':
    sample_sequence = [10, 25, 30, 45, 50]
    result = analyze_sequence(sample_sequence)
    print(result)