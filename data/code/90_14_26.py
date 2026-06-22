def evaluate_or_condition(a, b):
    return a or b

def process_sample(left, right):
    result = evaluate_or_condition(left, right)
    return result

if __name__ == '__main__':
    test_cases = {
        "numeric_zero_right": (0, 5),
        "numeric_one_right": (1, 0),
        "boolean_false_right": (False, True),
        "boolean_true_right": (True, False),
        "none_right": (None, "data"),
        "none_left": ("data", None),
        "empty_list_right": ([], [1]),
        "empty_list_left": ([1], []),
        "empty_string_right": ("", "text"),
        "empty_string_left": ("text", ""),
    }
    
    for name, (val_a, val_b) in test_cases.items():
        output = process_sample(val_a, val_b)
        print(output)