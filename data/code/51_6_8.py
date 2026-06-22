def generate_number_pyramid():
    levels = 4
    result = []
    for i in range(1, levels + 1):
        row_num = i
        row_str = str(row_num) * i
        padding = (levels - i) * 2
        centered_row = row_str.center(padding * 2 + i * len(str(1)) - 1)
        result.append(centered_row)
    return '\n'.join(result)

if __name__ == '__main__':
    print(generate_number_pyramid())