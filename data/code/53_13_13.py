def reverse_number_triangle(row_count):
    result = []
    for i in range(row_count, 0, -1):
        row_str = " ".join(str(j) for j in range(i, 0, -1))
        result.append(row_str)
    return "\n".join(result)

if __name__ == '__main__':
    rows = 5
    print(reverse_number_triangle(rows))