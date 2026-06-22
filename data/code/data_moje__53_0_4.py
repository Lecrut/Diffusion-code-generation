def generate_reverse_number_triangle(rows=5):
    return [f"{' '.join(str(j) for j in range(i, rows + 1)).center((2 * rows - 1) * 2)}" for i in range(1, rows + 1)]

if __name__ == '__main__':
    triangle = generate_reverse_number_triangle(5)
    for line in triangle:
        print(line.strip())