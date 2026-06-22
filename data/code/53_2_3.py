def reverse_number_triangle(height=6):
    result = []
    for i in range(height, 0, -1):
        row = ''
        for j in range(1, i + 1):
            row += str(j)
        result.append(row)
    return result

if __name__ == '__main__':
    print(reverse_number_triangle(6))