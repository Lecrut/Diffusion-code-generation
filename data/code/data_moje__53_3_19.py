def generate_reverse_triangle(rows):
    result = []
    for i in range(rows, 0, -1):
        line = ""
        for j in range(1, i + 1):
            line += str(j)
        result.append(line)
    return "\n".join(result)

if __name__ == '__main__':
    print(generate_reverse_triangle(5))