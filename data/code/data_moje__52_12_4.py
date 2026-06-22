def create_diamond_shape(r):
    if r <= 0:
        return ""
    rows = []
    for y in range(-r, r + 1):
        dist = abs(y)
        width = 2 * (r - dist) - 1
        padding = dist
        rows.append(" " * padding + "*" * width)
    return "\n".join(rows)

if __name__ == '__main__':
    print(create_diamond_shape(4))