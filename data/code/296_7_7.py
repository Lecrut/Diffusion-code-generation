def manipulate_ratio(a, b):
    initial_ratio = (a, b)
    ratio_halved = (a / 2, b)
    ratio_doubled = (2 * a, b)
    ratio_inverted = (b, a)
    return {
        "initial": initial_ratio,
        "halved": ratio_halved,
        "doubled": ratio_doubled,
        "inverted": ratio_inverted
    }
if __name__ == '__main__':
    a_val = 10
    b_val = 5
    results = manipulate_ratio(a_val, b_val)
    print(f"Initial ratio a:b is: {results['initial'][0]}:{results['initial'][1]}")
    print(f"Ratio after halving (a/2):(b): {results['halved'][0]}:{results['halved'][1]}")
    print(f"Ratio after doubling (2a):(b): {results['doubled'][0]}:{results['doubled'][1]}")
    print(f"Ratio after inverting (b):(a): {results['inverted'][0]}:{results['inverted'][1]}")