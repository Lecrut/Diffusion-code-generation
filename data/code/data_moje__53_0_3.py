def generate_reverse_number_triangle(rows=5):
    return [' '.join(str(j) for j in range(i, 0, -1)) for i in range(rows, 0, -1)]

if __name__ == '__main__':
    for line in generate_reverse_number_triangle(5):
        print(line)