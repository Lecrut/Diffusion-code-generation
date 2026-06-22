def generate_reverse_number_triangle(height: int) -> list[str]:
    if height <= 0:
        return []
    
    result = []
    for i in range(height, 0, -1):
        row = []
        for j in range(1, i + 1):
            row.append(str(j))
        result.append(" ".join(row))
    return result

if __name__ == '__main__':
    height = 5
    triangle = generate_reverse_number_triangle(height)
    for row in triangle:
        print(row)