def convert_ratios(ratios):
    results = []
    for a, b in ratios:
        if b == 0:
            results.append(float('inf') if a != 0 else float('nan'))
        else:
            results.append(a / b)
    return results
if __name__ == '__main__':
    sample_ratios = [
        (1000000000, 500000000),
        (123456789, 10),
        (0, 5),
        (10, 0),
        (1, 1)
    ]
    output = convert_ratios(sample_ratios)
    for ratio in output:
        print(ratio)