def evaluate_arithmetic_comparisons(comparisons):
    return [eval(comp) for comp in comparisons]

if __name__ == '__main__':
    sample_data = [("2 + 3 > 5", False), ("4 * 4 == 16", True), ("10 - 5 < 8", True)]
    results = evaluate_arithmetic_comparisons([comp[0] for comp in sample_data])
    print(results)