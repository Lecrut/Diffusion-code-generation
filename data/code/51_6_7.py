def generate_pyramid(levels: int) -> list:
    result = []
    for i in range(1, levels + 1):
        row_values = list(range(1, 2 ** i, 2))
        row_str = " ".join(str(x) for x in row_values)
        result.append(row_str)
    return result

if __name__ == '__main__':
    pyramid_lines = generate_pyramid(4)
    for line in pyramid_lines:
        print(line)