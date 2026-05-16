def resolve_decision_tree(node, value):
    if node == "A":
        if value > 10:
            return 1
        else:
            return 0
    elif node == "B":
        if value % 2 == 0:
            return 2
        else:
            return 3
    elif node == "C":
        if value < 5:
            return 4
        else:
            return 5
    else:
        return value
if __name__ == '__main__':
    test_cases = [
        (("A", 15), 1),
        (("A", 5), 0),
        (("B", 10), 2),
        (("B", 11), 3),
        (("C", 3), 4),
        (("C", 7), 5),
        (("D", 99), 99)
    ]
    for (node, val), expected in test_cases:
        result = resolve_decision_tree(node, val)
        print(f"Node: {node}, Value: {val}, Result: {result}, Expected: {expected}, Match: {result == expected}")