def build_or_truth_table():
    operands = [True, False]
    rows = []
    for left in operands:
        for right in operands:
            rows.append({"left": left, "right": right, "result": left or right})
    return rows

if __name__ == '__main__':
    truth_table = build_or_truth_table()
    print(truth_table)