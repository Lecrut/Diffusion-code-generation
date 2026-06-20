def get_opposite_truth(boolean_value: bool) -> bool:
    return not boolean_value

if __name__ == '__main__':
    original_true = True
    inverted_true = get_opposite_truth(original_true)
    print(f"Original: {original_true}, Opposite: {inverted_true}")

    original_false = False
    inverted_false = get_opposite_truth(original_false)
    print(f"Original: {original_false}, Opposite: {inverted_false}")