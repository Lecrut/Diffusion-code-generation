import math
def generate_diamond(size):
    lines = []
    for i in range(size * 2 - 1):
        line = ""
        left = max(0, size - abs(i - (size - 1)))
        right = size - left
        if i < size:
            stars = 2 * i + 1
            spaces = size - i
            line = " " * spaces + "*" * stars
        else:
            stars = 2 * (size - i) + 1
            spaces = i
            line = " " * spaces + "*" * stars
        lines.append(line)
    return lines
if __name__ == '__main__':
    diamond_size = 5
    pattern = generate_diamond(diamond_size)
    for line in pattern:
        print(line)