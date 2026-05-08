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
        if value < 5:
            return value * 3
        else:
            return value - 2
    else:
        return value
if __name__ == '__main__':
    tree_structure = {
        'A': {
            'condition': lambda v: v > 10,
            'true': lambda v: v * 2,
            'false': lambda v: v + 5
        },
        'B': {
            'condition': lambda v: v % 2 == 0,
            'true': lambda v: v // 2,
            'false': lambda v: v + 1
        },
        'C': {
            'condition': lambda v: v < 5,
            'true': lambda v: v * 3,
            'false': lambda v: v - 2
        }
    }
    def recursive_resolver(node_key, input_value):
        if node_key not in tree_structure:
            return input_value
        node_data = tree_structure[node_key]
        condition_func = node_data['condition']
        if condition_func(input_value):
            return node_data['true'](input_value)
        else:
            return node_data['false'](input_value)
    result1 = recursive_resolver('A', 15)
    result2 = recursive_resolver('A', 5)
    result3 = recursive_resolver('B', 10)
    result4 = recursive_resolver('B', 7)
    result5 = recursive_resolver('C', 3)
    result6 = recursive_resolver('C', 10)
    print(f"A(15): {result1}")
    print(f"A(5): {result2}")
    print(f"B(10): {result3}")
    print(f"B(7): {result4}")
    print(f"C(3): {result5}")
    print(f"C(10): {result6}")