def generate_reverse_triangle(rows):
    result = []
    for i in range(rows, 0, -1):
        row_numbers = [str(j) for j in range(1, i + 1)]
        row_string = " ".join(row_numbers)
        padded_row = row_string.center(rows * 2 - 1)
        result.append(padded_row)
    return "\n".join(result)

if __name__ == '__main__':
    print(generate_reverse_triangle(5))