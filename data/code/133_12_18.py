def evaluate_arithmetic_comparisons(comparison_list):
    bool_list = [eval(comp) for comp in comparison_list]
    return bool_list

if __name__ == '__main__':
    sample_data = ['1 + 2 == 3', '4 * 5 != 20', '6 > 7', '8 < 9']
    result = evaluate_arithmetic_comparisons(sample_data)
    print(result)