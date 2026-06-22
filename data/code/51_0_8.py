def generate_right_aligned_pyramid(rows):
    result = []
    for i in range(1, rows + 1):
        row = list(range(1, i + 1))
        formatted_row = ' '.join(str(num) for num in row)
        padded_row = formatted_row.rjust(rows * 2 - 1)
        result.append(padded_row)
    return '\n'.join(result)

if __name__ == '__main__':
    num_rows = 5
    output = generate_right_aligned_pyramid(num_rows)
    print(output)