TRUE_VAL = True
FALSE_VAL = False

def negate_boolean(value: bool) -> bool:
    if value is TRUE_VAL:
        return FALSE_VAL
    if value is FALSE_VAL:
        return TRUE_VAL
    raise ValueError(f"Expected bool, got {type(value).__name__}")

if __name__ == '__main__':
    input_true = True
    input_false = False
    output_negated_true = negate_boolean(input_true)
    output_negated_false = negate_boolean(input_false)
    print(output_negated_true)
    print(output_negated_false)