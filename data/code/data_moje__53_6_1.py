def reverse_number_triangle(height=4):
    lines = []
    for i in range(height, 0, -1):
        line = ' '.join(str(j) for j in range(1, i + 1))
        lines.append(line)
    return '\n'.join(lines)

if __name__ == '__main__':
    print(reverse_number_triangle(4))