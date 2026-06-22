def generate_reverse_triangle(rows=5):
    result = []
    current_num = 1
    for i in range(1, rows + 1):
        row = []
        for j in range(i):
            row.append(current_num)
            current_num += 1
        row.reverse()
        result.append(row)
    return result

if __name__ == '__main__':
    print(generate_reverse_triangle())