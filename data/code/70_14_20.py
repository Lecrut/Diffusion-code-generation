def get_extremes(input_list):
    if not input_list:
        raise ValueError("Input list must contain at least one element")
    return input_list[0], input_list[-1]

RESULT_LABELS = {
    "first": "first_element",
    "last": "last_element"
}

if __name__ == '__main__':
    test_data = [42, 99, 108, 2024]
    val_first, val_last = get_extremes(test_data)
    labels = RESULT_LABELS
    formatted_output = {
        labels["first"]: val_first,
        labels["last"]: val_last
    }
    print(formatted_output)