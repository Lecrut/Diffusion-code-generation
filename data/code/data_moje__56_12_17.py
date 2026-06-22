def build_multiplication_entries(base_integer, limit):
    computed_lines = []
    for current_multiplier in range(1, limit + 1):
        product_value = base_integer * current_multiplier
        formatted_entry = f"{base_integer} * {current_multiplier} = {product_value}"
        computed_lines.append(formatted_entry)
    return computed_lines

if __name__ == '__main__':
    target_number = 3
    row_limit = 10
    table_rows = build_multiplication_entries(target_number, row_limit)
    for each_row in table_rows:
        print(each_row)