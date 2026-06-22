def generate_symmetric_pyramid(row_count):
    rows = []
    for i in range(1, row_count + 1):
        left_part = list(range(1, i + 1))
        right_part = list(range(1, i + 1))
        right_part.reverse()
        right_part.pop(0)
        numbers = left_part + right_part
        row_string = "".join(str(num) for num in numbers)
        total_width = 2 * row_count - 1
        padding = (total_width - len(row_string)) // 2
        full_row = " " * padding + row_string
        rows.append(full_row)
    return "\n".join(rows)

if __name__ == '__main__':
    print(generate_symmetric_pyramid(8))