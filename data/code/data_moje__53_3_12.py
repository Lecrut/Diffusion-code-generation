def generate_reverse_number_triangle(rows):
    result = []
    for i in range(1, rows + 1):
        row_num = rows - i + 1
        row_str = ""
        for j in range(row_num):
            if j > 0:
                row_str += " "
            row_str += str(row_num)
        result.append(row_str)
    return "\n".join(result)

if __name__ == '__main__':
    print(generate_reverse_number_triangle(5))