BOOL_FALSE_VALUE = False
BOOL_TRUE_VALUE = True

def validate_both_negative(left_side, right_side):
    is_left_negative = left_side == BOOL_FALSE_VALUE
    is_right_negative = right_side == BOOL_FALSE_VALUE
    return is_left_negative and is_right_negative

if __name__ == '__main__':
    sample_left = BOOL_FALSE_VALUE
    sample_right = BOOL_FALSE_VALUE
    computed_result = validate_both_negative(sample_left, sample_right)
    print(computed_result)