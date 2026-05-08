def resolve_decision_tree(node, value):
    if node == "A":
        if value > 5:
            return 1
        else:
            return 2
    elif node == "B":
        if value % 2 == 0:
            return 3
        else:
            return 4
    elif node == "C":
        if value < 10:
            return 5
        else:
            return 6
    else:
        return 0
if __name__ == '__main__':
    test_cases = [
        ("A", 7),
        ("A", 3),
        ("B", 4),
        ("B", 6),
        ("C", 5),
        ("C", 15)
    ]
    for node, val in test_cases:
        result = resolve_decision_tree(node, val)
        print(f"Node: {node}, Value: {val}, Result: {result}")