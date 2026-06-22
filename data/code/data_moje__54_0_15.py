def generate_hollow_square(size):
    if size <= 0:
        return ""
    if size == 1:
        return "*"
    result = []
    for i in range(size):
        row = []
        for j in range(size):
            if i == 0 or i == size - 1 or j == 0 or j == size - 1:
                row.append("*")
            else:
                row.append(" ")
        result.append("".join(row))
    return "\n".join(result)

if __name__ == '__main__':
    size = 5
    square = generate_hollow_square(size)
    print(square)