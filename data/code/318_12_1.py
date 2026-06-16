def compare_adjacent_pairs(numbers):
    report = []
    for i in range(len(numbers) - 1):
        a = numbers[i]
        b = numbers[i+1]
        if a < b:
            comparison = "strictly less than"
        elif a >= b:
            comparison = "greater than or equal to"
        else:
            comparison = "equal to"
        report.append((a, b, comparison))
    return report
if __name__ == '__main__':
    sample_numbers = [1.5, 3.0, 2.5, 2.5, 8.1, 8.1, 7.9]
    comparison_results = compare_adjacent_pairs(sample_numbers)
    print("--- Adjacent Pair Comparison Report ---")
    for a, b, comparison in comparison_results:
        print(f"Comparing {a} and {b}: {comparison}")