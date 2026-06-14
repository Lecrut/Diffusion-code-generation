import math
def generate_diamond(size):
    lines = []
    for i in range(size * 2 - 1):
        line = ""
        left = max(0, size - abs(i - (size - 1)))
        right = size + abs(i - (size - 1)) - left
        if i < size:
            padding = size - 1 - i
            stars = 2 * padding + 1
            spaces = size - stars
            line = " " * spaces + "*" * stars + " " * spaces
        else:
            padding = i - (size - 1)
            stars = 2 * (size - 1 - padding) + 1
            spaces = size - stars
            line = " " * spaces + "*" * stars + " " * spaces
        if line:
            lines.append(line)
    return lines
def generate_symmetrical_diamond(n):
    diamond_lines = []
    center = n // 2
    max_radius = n - 1
    for r in range(n):
        row = ""
        if r <= center:
            spaces = center - r
            stars = 2 * r + 1
            row = " " * spaces + "*" * stars + " " * spaces
        else:
            spaces = r - center
            stars = 2 * (max_radius - r) + 1
            row = " " * spaces + "*" * stars + " " * spaces
        diamond_lines.append(row)
    return diamond_lines
if __name__ == '__main__':
    sample_size = 5
    pattern = generate_symmetrical_diamond(sample_size)
    for line in pattern:
        print(line)