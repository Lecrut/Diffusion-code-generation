def get_or_truth_table():
    operands = [True, False]
    return [
        {"x": a, "y": b, "x | y": a | b}
        for a in operands
        for b in operands
    ]

if __name__ == '__main__':
    print(get_or_truth_table())