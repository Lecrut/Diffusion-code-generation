def flatten_boolean_logic(nested_structure):
    def flatten(item):
        if isinstance(item, bool):
            return item
        elif isinstance(item, list) or isinstance(item, tuple):
            return all(flatten(sub_item) for sub_item in item)
        else:
            raise ValueError("Unsupported data type encountered")

    return flatten(nested_structure)

if __name__ == '__main__':
    sample_structure = [
        True,
        [False, True],
        [True, [False, False]],
        True
    ]
    result = flatten_boolean_logic(sample_structure)
    print(f"Flattened Result: {result}")