def reverse_number_triangle(height):
    result = []
    for i in range(height, 0, -1):
        row = [str(j) for j in range(1, i + 1)]
        result.append(" ".join(row))
    return result

if __name__ == '__main__':
    height = 6
    print(reverse_number_triangle(height))