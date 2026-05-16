def resolve_decision_tree(node, decision_value):
    if node == "A":
        if decision_value > 5:
            return 1
        else:
            return 2
    elif node == "B":
        if decision_value == 10:
            return 3
        else:
            return 4
    elif node == "C":
        if decision_value % 2 == 0:
            return 5
        else:
            return 6
    else:
        return 0
if __name__ == '__main__':
    test_cases = [
        (("A", 7), 1),
        (("A", 3), 2),
        (("B", 10), 3),
        (("B", 5), 4),
        (("C", 4), 5),
        (("C", 3), 6),
        (("D", 1), 0)
    ]
    for (node, decision), expected in test_cases:
        result = resolve_decision_tree(node, decision)
        assert result == expected, f"Input: node={node}, decision={decision}, Expected: {expected}, Got: {result}"
        print(f"Test Passed for node={node}, decision={decision}. Result: {result}")