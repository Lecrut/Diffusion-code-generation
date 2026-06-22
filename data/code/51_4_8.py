def generate_number_pyramid():
    lines = []
    for row in range(1, 4):
        padding = " " * (3 - row)
        numbers = " ".join(str(n) for n in range(1, row + 1))
        lines.append(padding + numbers)
    return "\n".join(lines)

if __name__ == "__main__":
    result = generate_number_pyramid()
    print(result)