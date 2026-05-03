def convert_ratios(ratios):
    results = []
    for a, b in ratios:
        if b == 0:
            results.append(float('inf') if a != 0 else float('nan'))
        else:
            results.append(a / b)
    return results
if __name__ == '__main__':
    input_ratios = [
        (1000000000, 500000000),
        (1234567890123, 9876543210987),
        (0, 100),
        (5, 0),
        (10, 2)
    ]
    output = convert_ratios(input_ratios)
    print(output)