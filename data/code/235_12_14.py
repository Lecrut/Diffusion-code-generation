CHARACTER = '*'
SPACE = ' '

def generate_pyramid_line(n):
    lines = []
    for i in range(1, n + 1):
        line = (SPACE * (n - i)) + (CHARACTER * (2 * i - 1))
        lines.append(line)
    return "\n".join(lines)

if __name__ == '__main__':
    sample_number = 5
    pattern = generate_pyramid_line(sample_number)
    print(pattern)