def resolve_decision_tree(node, value):
    if node == 'A':
        if value > 10:
            return value * 2
        else:
            return value + 5
    elif node == 'B':
        if value % 2 == 0:
            return value // 2
        else:
            return value + 1
    elif node == 'C':
        if value < 0:
            return value * -1
        else:
            return value
    else:
        return value
if __name__ == '__main__':
    tree1 = 'A'
    value1 = 15
    result1 = resolve_decision_tree(tree1, value1)
    print(f"Result 1: {result1}")
    tree2 = 'B'
    value2 = 10
    result2 = resolve_decision_tree(tree2, value2)
    print(f"Result 2: {result2}")
    tree3 = 'C'
    value3 = -5
    result3 = resolve_decision_tree(tree3, value3)
    print(f"Result 3: {result3}")
    tree4 = 'A'
    value4 = 5
    result4 = resolve_decision_tree(tree4, value4)
    print(f"Result 4: {result4}")
    tree5 = 'B'
    value5 = 7
    result5 = resolve_decision_tree(tree5, value5)
    print(f"Result 5: {result5}")