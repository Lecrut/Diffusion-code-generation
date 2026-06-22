def reverse_number_triangle(n: int) -> str:
    lines = []
    for i in range(n, 0, -1):
        lines.append(' '.join(str(j) for j in range(1, i + 1)))
    return '\n'.join(lines)

if __name__ == '__main__':
    print(reverse_number_triangle(5))