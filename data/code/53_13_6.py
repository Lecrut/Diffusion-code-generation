def generate_reverse_number_triangle(rows):
    if rows <= 0:
        return []
    
    triangle = []
    current_number = rows * (rows + 1) // 2
    
    for i in range(rows, 0, -1):
        row = []
        for j in range(i):
            row.append(current_number)
            current_number -= 1
        triangle.append(row)
    
    return triangle

if __name__ == '__main__':
    result = generate_reverse_number_triangle(5)
    for row in result:
        print(' '.join(map(str, row)))