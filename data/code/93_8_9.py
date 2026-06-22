def are_inputs_false(left: bool, right: bool) -> bool:
    neg_left = not left
    neg_right = not right
    return neg_left and neg_right

if __name__ == '__main__':
    sample_a = False
    sample_b = True
    is_false = are_inputs_false(sample_a, sample_b)
    print(is_false)