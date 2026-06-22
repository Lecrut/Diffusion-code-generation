MULTIPLIER = 7
TABLE_WIDTH = 10
SEPARATOR = ' x '
EQUALS = ' = '

def get_multiplication_table():
    rows = []
    current_index = 1
    while current_index <= TABLE_WIDTH:
        product = MULTIPLIER * current_index
        row_text = str(MULTIPLIER) + SEPARATOR + str(current_index) + EQUALS + str(product)
        rows.append(row_text)
        current_index += 1
    return '\n'.join(rows)

if __name__ == '__main__':
    table_output = get_multiplication_table()
    print(table_output)