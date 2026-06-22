def build_symmetric_pyramid(rows=6):
    max_width = 2 * rows - 1
    result = []
    for i in range(1, rows + 1):
        num = i
        row_nums = []
        for j in range(1, i + 1):
            row_nums.append(str(j))
        for j in range(i - 2, 0, -1):
            row_nums.append(str(j))
        row_str = "".join(row_nums)
        padding = (max_width - len(row_str)) // 2
        line = " " * padding + row_str + " " * padding
        result.append(line)
    return "\n".join(result)

if __name__ == '__main__':
    print(build_symmetric_pyramid(6))