def hollow_square(size):
    if size <= 0:
        return ""
    if size == 1:
        return "*"
    top_bottom = "*" * size
    middle = "*" + " " * (size - 2) + "*"
    lines = [top_bottom]
    lines.extend([middle] * (size - 2))
    lines.append(top_bottom)
    return "\n".join(lines)

if __name__ == '__main__':
    print(hollow_square(10))