def evaluate_arithmetic_comparisons(comparisons):
    return [eval(comp) for comp in comparisons]

if __name__ == '__main__':
    sample_data = [("2 + 3 == 5",), ("4 * 2 != 9",), ("10 - 5 < 6",)]
    results = evaluate_arithmetic_comparisons(sample_data)
    print(results)