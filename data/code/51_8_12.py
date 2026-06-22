def print_number_pyramid(rows=5):
    result = []
    for i in range(1, rows + 1):
        line = ""
        for j in range(1, i + 1):
            line += str(j)
        result.append(line)
    return "\n".join(result)

if __name__ == '__main__':
    print(print_number_pyramid())