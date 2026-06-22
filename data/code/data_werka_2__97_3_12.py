def get_implication_result(p, q):
    truth_values = [False, True]
    table = []
    for p_val in truth_values:
        for q_val in truth_values:
            result = (not p_val) or q_val
            table.append({
                "P": p_val,
                "Q": q_val,
                "Result": result
            })
    return table

def display_table(rows):
    for row in rows:
        print(f"P={row['P']}, Q={row['Q']}, P -> Q={row['Result']}")

if __name__ == '__main__':
    table_data = get_implication_result(False, False)
    display_table(table_data)