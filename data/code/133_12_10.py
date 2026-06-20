def evaluate_arithmetic_comparisons(comparison_list):
    return [eval(comp) for comp in comparison_list]

if __name__ == '__main__':
    sample_data = [('2 + 2 == 4'), ('3 * 3 != 9'), ('5 > 10')]
    print(evaluate_arithmetic_comparisons(sample_data))