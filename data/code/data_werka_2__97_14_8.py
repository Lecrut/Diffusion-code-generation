def generate_or_truth_table():
    inputs = [True, False]
    result = []
    for a in inputs:
        for b in inputs:
            result.append({"A": a, "B": b, "A OR B": a or b})
    return result

if __name__ == '__main__':
    print(generate_or_truth_table())