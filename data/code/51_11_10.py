def build_number_pyramid(height):
    lines = []
    for i in range(1, height + 1):
        spaces = " " * (height - i)
        numbers = " ".join(str(j) for j in range(1, i + 1))
        lines.append(f"{spaces}{numbers}")
    return "\n".join(lines)

if __name__ == '__main__':
    pyramid = build_number_pyramid(7)
    print(pyramid)