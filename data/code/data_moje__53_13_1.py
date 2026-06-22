def reverse_number_triangle(rows):
    result = []
    current_num = rows
    while current_num > 0:
        line = str(current_num) * current_num
        result.append(line)
        current_num -= 1
    return '\n'.join(result)

if __name__ == '__main__':
    sample_rows = 5
    print(reverse_number_triangle(sample_rows))