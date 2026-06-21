def calculate_truth_values():
    results = []
    for A in [False, True]:
        for B in [False, True]:
            for C in [False, True]:
                for D in [False, True]:
                    result = (A or B) and (C or D)
                    results.append((A, B, C, D, result))
    return results

if __name__ == '__main__':
    truth_values = calculate_truth_values()
    for A, B, C, D, result in truth_values:
        print(f"A={A}, B={B}, C={C}, D={D} -> {result}")