def create_or_truth_table():
    inputs = [True, False]
    table = []
    for a in inputs:
        for b in inputs:
            table.append({"a": a, "b": b, "a or b": a or b})
    return table

if __name__ == '__main__':
    result = create_or_truth_table()
    print(result)