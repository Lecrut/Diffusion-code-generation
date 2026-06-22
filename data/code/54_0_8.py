def hollow_square(size):
    if size <= 0:
        return ""
    if size == 1:
        return "*"
    lines = []
    for i in range(size):
        if i == 0 or i == size - 1:
            lines.append("*" * size)
        else:
            lines.append("*" + " " * (size - 2) + "*")
    return "\n".join(lines)

if __name__ == '__main__':
    result = hollow_square(5)
    print(result)