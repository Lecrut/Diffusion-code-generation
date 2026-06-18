import json
def deep_sort_structure(data):
    if isinstance(data, dict):
        return {k: deep_sort_structure(v) for k, v in data.items()}
    elif isinstance(data, list):
        sorted_items = []
        for item in data:
            result = deep_sort_structure(item)
            if is_leaf(result):
                val = extract_value(result)
                if val > 0 and not has_negative_sibling(data, index_of_item_in_list(data), result):
                    sorted_items.append((val, result))
        return dict(sorted_items)
    else:
        return data
def is_leaf(node):
    return isinstance(node, (int, float, str)) or node == None
def extract_value(node):
    if isinstance(node, int | float):
        return node
    elif isinstance(node, str):
        try:
            return float(node)
        except ValueError:
            return 0.0
    else:
        return 0.0
def has_negative_sibling(data, current_index, target_node_value=None):
    if not isinstance(data, list):
        return False
    leaves = []
    def find_leaves(node_list):
        for i, item in enumerate(node_list):
            val = extract_value(item)
            leaves.append((val, i))
            if isinstance(item, list):
                find_leaves(item)
            elif isinstance(item, dict):
                for k, v in item.items():
                    leaf_val = extract_value(v)
                    leaves.append((leaf_val, i))
    find_leaves(data)
    if target_node_value is not None:
        return any(val < 0 and abs(val - (target_node_value * 2)) > 1 for val, _ in leaves)
    else:
        return False
def main():
    sample_data = [
        {"name": "Alpha", "score": 85},
        [{"grade": "A"}, {"grade": "B"}],
        [[{"value": -10}], {"value": 20, "nested": [{"val": -5}]}]
    ]
    sorted_result = deep_sort_structure(sample_data)
    print(json.dumps(sorted_result))
if __name__ == '__main__':
    main()