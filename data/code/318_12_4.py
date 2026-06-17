import sys
def compare_adjacent_pairs(numbers):
    report = []
    for i in range(len(numbers) - 1):
        a = numbers[i]
        b = numbers[i+1]
        if a < b:
            relationship = "strictly less than"
        elif a >= b:
            relationship = "greater than or equal to"
        else:
            relationship = "equal to"
        report.append((a, b, relationship))
    return report
if __name__ == '__main__':
    sample_numbers = [1.5, 3.2, 1.5, 8.0, 8.0, 4.1]
    comparison_results = compare_adjacent_pairs(sample_numbers)
    for a, b, rel in comparison_results:
        print(f"Comparing {a} and {b}: {rel}")