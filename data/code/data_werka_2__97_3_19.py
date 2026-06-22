def get_implication_result(p_value, q_value):
    if not (isinstance(p_value, bool) and isinstance(q_value, bool)):
        raise ValueError("Inputs must be boolean")
    if p_value and not q_value:
        return False
    return True

def construct_implication_table():
    truth_values = [False, True]
    table_data = []
    for p_val in truth_values:
        for q_val in truth_values:
            result_val = get_implication_result(p_val, q_val)
            table_data.append((p_val, q_val, result_val))
    return table_data

def display_table_rows(rows):
    output_lines = []
    for p, q, res in rows:
        line = f"P={p} Q={q} P -> Q={res}"
        output_lines.append(line)
    return "\n".join(output_lines)

if __name__ == '__main__':
    computed_table = construct_implication_table()
    formatted_output = display_table_rows(computed_table)
    print(formatted_output)