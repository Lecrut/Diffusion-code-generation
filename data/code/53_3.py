def generate_reverse_number_triangle(rows=5):
    result = []
    for i in range(rows):
        row = []
        for j in range(rows - 1, -1, -1):
            if i == 0:
                row.append(str(j))
            else:
                row.append(str(j))
        result.append(" ".join(row))
    return "\n".join(result)

if __name__ == '__main__':
    print(generate_reverse_number_triangle())