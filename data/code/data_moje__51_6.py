def generate_number_pyramid(levels):
    pyramid = []
    for i in range(1, levels + 1):
        row = [2 ** i - 2 + k for k in range(2 ** (i - 1))]
        pyramid.append(row)
    return pyramid

def format_pyramid(pyramid):
    output_lines = []
    max_width = 0
    if pyramid:
        last_row = pyramid[-1]
        last_row_str = " ".join(map(str, last_row))
        max_width = len(last_row_str)
    for row in pyramid:
        row_str = " ".join(map(str, row))
        padding = (max_width - len(row_str)) // 2
        output_lines.append(" " * padding + row_str)
    return "\n".join(output_lines)

if __name__ == "__main__":
    result = generate_number_pyramid(4)
    print(format_pyramid(result))