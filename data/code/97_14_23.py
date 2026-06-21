def generate_or_truth_table():
    VALID_INPUTS = [True, False]

    def validate_operand(value):
        if value not in (True, False):
            raise ValueError("Operand must be a boolean")
        return value

    def combine_or(a, b):
        val_a = validate_operand(a)
        val_b = validate_operand(b)
        return val_a or val_b

    result_rows = []
    for x in VALID_INPUTS:
        for y in VALID_INPUTS:
            row = {"x": x, "y": y, "x | y": combine_or(x, y)}
            result_rows.append(row)
    return result_rows

if __name__ == '__main__':
    print(generate_or_truth_table())