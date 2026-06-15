import math
def generate_diamond(size):
    lines = []
    for i in range(size * 2 - 1):
        line = ""
        left = max(0, size - abs(i - (size - 1)))
        right = size + abs(i - (size - 1)) - left
        if i < size:
            padding = size - 1 - i
            stars = 2 * i + 1
            line = "*" * stars
        else:
            padding = i - (size - 1)
            stars = 2 * (size - 1 - padding) + 1
            line = "*" * stars
        if i < size:
            line = "*" * (2 * i + 1)
        else:
            line = "*" * (2 * (size - 1 - (i - (size - 1))) + 1)
    diamond = []
    for r in range(size):
        row = ""
        for c in range(2 * size - 1):
            dist = abs(r - size // 2)
            if dist <= size // 2:
                if abs(c - (size - 1)) == dist:
                    row += "*"
                else:
                    row += " "
            else:
                row += " "
        diamond.append(row)
    return diamond
def generate_symmetrical_diamond(n):
    pattern = []
    center = n // 2
    for i in range(n):
        row = ""
        for j in range(2 * n - 1):
            dist = abs(i - center)
            if dist <= n - 1 - dist:
                if abs(j - (n - 1)) == dist:
                    row += "*"
                else:
                    row += " "
            else:
                row += " "
        pattern.append(row)
    return pattern
def generate_diamond_optimized(n):
    rows = []
    center = n // 2
    for i in range(n):
        row = ""
        for j in range(2 * n - 1):
            dist_from_center = abs(i - center)
            dist_from_center_j = abs(j - (n - 1))
            if dist_from_center <= n - 1 - dist_from_center:
                if dist_from_center_j == dist_from_center:
                    row += "*"
                else:
                    row += " "
            else:
                row += " "
        rows.append(row)
    return rows
if __name__ == '__main__':
    sample_size = 5
    diamond_pattern = generate_diamond_optimized(sample_size)
    for row in diamond_pattern:
        print(row)