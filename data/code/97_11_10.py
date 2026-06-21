def build_or_table(pairs):
    if not pairs:
        return []
    table = []
    for pair in pairs:
        if not isinstance(pair, (list, tuple)) or len(pair) != 2:
            raise ValueError("Input must be a list of pairs")
        x, y = pair
        table.append([x, y, x or y])
    return table

if __name__ == '__main__':
    inputs = [[True, False], [False, True], [True, True], [False, False]]
    result = build_or_table(inputs)
    print(result)