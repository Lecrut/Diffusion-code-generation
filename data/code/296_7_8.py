def manipulate_ratio(a, b):
    initial_ratio = (a, b)
    ratio_halved = (a / 2, b)
    ratio_doubled = (2 * a, b)
    ratio_inverted = (b, a)
    return initial_ratio, ratio_halved, ratio_doubled, ratio_inverted
if __name__ == '__main__':
    a_val = 10
    b_val = 4
    initial, halved, doubled, inverted = manipulate_ratio(a_val, b_val)
    print(f"Initial Ratio: {initial[0]}:{initial[1]}")
    print(f"Halved Ratio (a/2 : b): {halved[0]}:{halved[1]}")
    print(f"Doubled Ratio (2a : b): {doubled[0]}:{doubled[1]}")
    print(f"Inverted Ratio (b : a): {inverted[0]}:{inverted[1]}")