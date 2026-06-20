def evaluate_arithmetic_comparisons(comparison_list):
    return [eval(comp) for comp in comparison_list]

if __name__ == '__main__':
    sample_data = [("2 + 3 > 5", False), ("4 * 4 == 16", True), ("8 / 2 < 5", False)]
    results = evaluate_arithmetic_comparisons([comp[0] for comp in sample_data])
    print(results)