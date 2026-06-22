def generate_pyramid(n):
    lines = []
    for i in range(1, n + 1):
        chars = [chr(ord('A') + j) for j in range(i)]
        line = ''.join(chars)
        lines.append(line.center(n * 2 - 1))
    return '\n'.join(lines)

if __name__ == '__main__':
    print(generate_pyramid(5))