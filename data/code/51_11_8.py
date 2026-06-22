def build_pyramid(height):
    pyramid = []
    for row in range(1, height + 1):
        spaces = " " * (height - row)
        numbers = " ".join(str(i) for i in range(1, 2 * row))
        line = f"{spaces}{numbers}"
        pyramid.append(line)
    return "\n".join(pyramid)

if __name__ == '__main__':
    result = build_pyramid(7)
    print(result)