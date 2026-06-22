def reverse_number_triangle(height=6):
    lines = []
    for i in range(height, 0, -1):
        row_nums = [str(j) for j in range(i, 0, -1)]
        row = " ".join(row_nums)
        lines.append(row)
    return lines

if __name__ == '__main__':
    result = reverse_number_triangle(6)
    print(result)