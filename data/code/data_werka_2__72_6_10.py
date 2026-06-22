def compare_and_label(list1, list2):
    relation_map = {
        -1: "less",
        0: "equal",
        1: "greater"
    }
    output = []
    for val1, val2 in zip(list1, list2):
        if val1 < val2:
            code = -1
        elif val1 > val2:
            code = 1
        else:
            code = 0
        label = relation_map[code]
        output.append((val1, val2, label))
    return output

if __name__ == '__main__':
    source_data = [10, 20, 30]
    target_data = [10, 15, 35]
    comparisons = compare_and_label(source_data, target_data)
    for pair in comparisons:
        print(pair)