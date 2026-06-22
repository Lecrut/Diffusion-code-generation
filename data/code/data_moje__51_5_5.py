def build_hollow_pyramid(rows):
    if rows <= 0:
        return []
    
    result = []
    for i in range(1, rows + 1):
        row_str = ""
        for j in range(1, 2 * i):
            if i == 1:
                row_str += "*"
            elif i == rows or j == 1 or j == 2 * i - 1:
                row_str += "*"
            else:
                row_str += " "
        result.append(row_str)
    
    return result

if __name__ == '__main__':
    sample_rows = 5
    pattern = build_hollow_pyramid(sample_rows)
    for line in pattern:
        print(line)