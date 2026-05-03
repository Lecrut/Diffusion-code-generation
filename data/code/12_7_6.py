import math
def convert_ratios(ratios):
    result = []
    for a, b in ratios:
        if b == 0:
            result.append(float('inf') if a != 0 else float('nan'))
        else:
            result.append(a / b)
    return result
if __name__ == '__main__':
    sample_ratios = [
        (1000000000, 500000000),
        (1234567890123, 9876543210987),
        (0, 100),
        (5, 0),
        (10, 2)
    ]
    converted = convert_ratios(sample_ratios)
    for ratio in converted:
        print(ratio)