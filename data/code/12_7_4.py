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
        (1234567890123, 1000000000000),
        (0, 5),
        (10, 0),
        (12345, 6789)
    ]
    output = convert_ratios(sample_ratios)
    print(output)