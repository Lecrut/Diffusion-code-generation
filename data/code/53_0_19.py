def generate_reverse_triangle(max_rows):
    return [" ".join(str(j) for j in range(i, 0, -1)) for i in range(max_rows, 0, -1)]

if __name__ == '__main__':
    result = generate_reverse_triangle(5)
    for line in result:
        print(line)