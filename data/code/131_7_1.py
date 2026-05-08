def resolve_decision_tree(node, value):
    if node == "A":
        if value > 10:
            return value * 2
        else:
            return value + 5
    elif node == "B":
        if value % 2 == 0:
            return value // 2
        else:
            return value + 1
    elif node == "C":
        if value < 5:
            return value - 1
        else:
            return value * 3
    else:
        return value
if __name__ == '__main__':
    test_cases = [
        (("A", 15), 30),
        (("A", 5), 10),
        (("B", 10), 5),
        (("B", 7), 8),
        (("C", 3), 2),
        (("C", 8), 24),
        (("D", 100), 100)
    ]
    for (node, value), expected in test_cases:
        result = resolve_decision_tree(node, value)
        print(f"Node: {node}, Value: {value}, Result: {result}, Expected: {expected}, Match: {result == expected}")