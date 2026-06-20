def evaluate_arithmetic_comparisons(comparison_list):
    results = []
    for comparison in comparison_list:
        if eval(comparison):
            results.append(True)
        else:
            results.append(False)
    return results

if __name__ == '__main__':
    sample_data = [
        "1 + 1 == 2",
        "3 * 3 != 9",
        "5 > 3",
        "7 <= 8",
        "10 == 10"
    ]
    result = evaluate_arithmetic_comparisons(sample_data)
    print(result)