def generate_left_aligned_reverse_number_triangle(rows):
    result = []
    for i in range(rows, 0, -1):
        line = ''
        for j in range(i):
            line += str(j + 1)
        result.append(line)
    return '\n'.join(result)

if __name__ == '__main__':
    print(generate_left_aligned_reverse_number_triangle(5))