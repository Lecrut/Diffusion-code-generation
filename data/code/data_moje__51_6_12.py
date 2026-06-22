def generate_number_pyramid(levels: int) -> str:
    result = []
    for i in range(1, levels + 1):
        row_values = [str(j) for j in range(1, i + 1)]
        row_string = " ".join(row_values)
        padding = " " * ((levels - i) * 2)
        result.append(padding + row_string)
    return "\n".join(result)

if __name__ == '__main__':
    print(generate_number_pyramid(4))