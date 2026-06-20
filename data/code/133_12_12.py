def evaluate_arithmetic_comparisons(comparison_list):
    return [eval(comp) for comp in comparison_list]

if __name__ == '__main__':
    sample_data = [("2 + 3 == 5",), ("4 * 2 != 8",), ("10 > 5",)]
    print(evaluate_arithmetic_comparisons(sample_data))