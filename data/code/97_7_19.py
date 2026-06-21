def _validate_variable_names(variables):
    if not isinstance(variables, (list, tuple)):
        raise ValueError("variables must be a list or tuple")
    if len(variables) == 0:
        raise ValueError("variables list cannot be empty")
    if len(variables) != len(set(variables)):
        raise ValueError("variable names must be unique")
    for var in variables:
        if not isinstance(var, str):
            raise ValueError("variable names must be strings")
        if not var.isidentifier():
            raise ValueError(f"invalid variable name: {var}")
    return variables

def generate_truth_table(variables):
    validated_vars = _validate_variable_names(variables)
    n = len(validated_vars)
    total_combinations = 1 << n
    rows = []
    for i in range(total_combinations):
        row = []
        for j in range(n):
            mask = 1 << (n - 1 - j)
            bit = (i & mask) != 0
            row.append(bit)
        rows.append(row)
    return validated_vars, rows

if __name__ == '__main__':
    var_names = ['p', 'q', 'r']
    headers, table_rows = generate_truth_table(var_names)
    print(headers)
    print(table_rows)