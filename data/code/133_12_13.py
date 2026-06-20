def evaluate_comparisons(comparison_list):
    return [eval(comp) for comp in comparison_list]

if __name__ == '__main__':
    sample_data = [('2 + 3 > 5',), ('4 * 4 == 16',), ('10 < 20',)]
    results = evaluate_comparisons([comp[0] for comp in sample_data])
    print(results)