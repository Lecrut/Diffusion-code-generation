import itertools

def generate_truth_table(inputs, expression):
    if not isinstance(inputs, (list, tuple)):
        raise ValueError("inputs must be a list or tuple")
    if len(inputs) < 1:
        raise ValueError("inputs must contain at least one element")
    if not callable(expression):
        raise ValueError("expression must be callable")
    n = len(inputs)
    total_rows = 2 ** n
    headers = list(inputs) + ['Result']
    col_width = max(len(str(h)) for h in headers)
    if col_width < 1:
        col_width = 1
    sep = ' | '
    header_line = sep.join(str(h).ljust(col_width) for h in headers)
    print(header_line)
    print(sep.join('-' * col_width for _ in headers))
    rows = itertools.product([0, 1], repeat=n)
    for row in rows:
        values = [bool(v) for v in row]
        result = expression(*values)
        row_str = sep.join(str(v).ljust(col_width) for v in values) + sep + str(bool(result)).ljust(col_width)
        print(row_str)

if __name__ == '__main__':
    vars_list = ['A', 'B', 'C', 'D']
    logic_func = lambda A, B, C, D: (A and B) or (C and not D)
    generate_truth_table(vars_list, logic_func)