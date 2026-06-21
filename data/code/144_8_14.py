def calculate_truth_values():
    results = []
    for A in [True, False]:
        for B in [True, False]:
            for C in [True, False]:
                for D in [True, False]:
                    result = (A or B) and (C or D)
                    results.append((A, B, C, D, result))
    return results

if __name__ == '__main__':
    truth_values = calculate_truth_values()
    print(truth_values)