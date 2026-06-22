import math

def generate_diamond(height):
    lines = []
    for i in range(1, height + 1):
        half = height // 2 + 1
        if i <= half:
            spaces = half - i
            stars = 2 * i - 1
        else:
            spaces = i - half
            stars = 2 * (height - i + 1) - 1
        line = ' ' * spaces + '*' * stars + ' ' * spaces
        lines.append(line)
    return lines

if __name__ == '__main__':
    height = 5
    result = generate_diamond(height)
    for line in result:
        print(line)