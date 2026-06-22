from functools import reduce

STAR_CHAR = "*"
DEFAULT_SIZE = 5

def generate_square_pattern(length):
    rows = []
    current_row = ""
    for col_index in range(length):
        current_row += STAR_CHAR
    for row_index in range(length):
        rows.append(current_row)
    return "\n".join(rows)

if __name__ == '__main__':
    side_dimension = 5
    result_string = generate_square_pattern(side_dimension)
    print(result_string)