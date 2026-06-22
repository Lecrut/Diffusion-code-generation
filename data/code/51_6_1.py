def generate_number_pyramid(levels):
    rows = []
    for i in range(levels):
        row = []
        for j in range(i + 1):
            row.append(j + 1)
        rows.append(row)
    return rows

def format_pyramid(rows):
    result_lines = []
    for i, row in enumerate(rows):
        padded_row = " ".join(str(num) for num in row)
        result_lines.append(padded_row.center(len(rows[-1]) * 2 - 1))
    return "\n".join(result_lines)

if __name__ == '__main__':
    pyramid_rows = generate_number_pyramid(4)
    formatted_pyramid = format_pyramid(pyramid_rows)
    print(formatted_pyramid)