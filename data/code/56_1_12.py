def generate_multiplication_table(max_num):
    row_strings = []
    header = ""
    for i in range(1, max_num + 1):
        header += f"{i:^{max_num * 2 + 1}}"
    row_strings.append(header)
    separator = "".join(["-" * (max_num * 2 + 1)] * max_num)
    row_strings.append(separator)
    for i in range(1, max_num + 1):
        row = ""
        for j in range(1, max_num + 1):
            row += f"{i * j:^{max_num * 2 + 1}}"
        row_strings.append(row)
    return "\n".join(row_strings)

if __name__ == '__main__':
    print(generate_multiplication_table(12))