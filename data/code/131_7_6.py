def resolve_decision_tree(node, value):
    if node == "A":
        if value > 10:
            return value * 2
        else:
            return value + 1
    elif node == "B":
        if value % 2 == 0:
            return value // 2
        else:
            return value + 5
    elif node == "C":
        if value > 50:
            return value - 10
        else:
            return value * 3
    else:
        return value
if __name__ == '__main__':
    tree_structure = {
        "A": {
            "condition": "value > 10",
            "true_branch": lambda v: v * 2,
            "false_branch": lambda v: v + 1
        },
        "B": {
            "condition": "value % 2 == 0",
            "true_branch": lambda v: v // 2,
            "false_branch": lambda v: v + 5
        },
        "C": {
            "condition": "value > 50",
            "true_branch": lambda v: v - 10,
            "false_branch": lambda v: v * 3
        }
    }
    def recursive_resolver(current_node, input_value):
        if current_node is None:
            return input_value
        if current_node in tree_structure:
            branch_key = tree_structure[current_node]["condition"]
            if "A" in current_node:
                if input_value > 10:
                    return tree_structure["A"]["true_branch"](input_value)
                else:
                    return tree_structure["A"]["false_branch"](input_value)
            elif "B" in current_node:
                if input_value % 2 == 0:
                    return tree_structure["B"]["true_branch"](input_value)
                else:
                    return tree_structure["B"]["false_branch"](input_value)
            elif "C" in current_node:
                if input_value > 50:
                    return tree_structure["C"]["true_branch"](input_value)
                else:
                    return tree_structure["C"]["false_branch"](input_value)
            else:
                return input_value
        return input_value
    result1 = recursive_resolver("A", 15)
    result2 = recursive_resolver("B", 8)
    result3 = recursive_resolver("C", 60)
    result4 = recursive_resolver("C", 40)
    result5 = recursive_resolver("D", 100)
    print(f"Result 1 (A, 15): {result1}")
    print(f"Result 2 (B, 8): {result2}")
    print(f"Result 3 (C, 60): {result3}")
    print(f"Result 4 (C, 40): {result4}")
    print(f"Result 5 (D, 100): {result5}")