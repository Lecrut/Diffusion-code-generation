def generate_number_pyramid(rows: int) -> str:
    lines = []
    for i in range(1, rows + 1):
        spaces = " " * (rows - i)
        numbers = " ".join(str(j) for j in range(1, i + 1))
        lines.append(f"{spaces}{numbers}")
    return "\n".join(lines)

if __name__ == "__main__":
    height = 5
    print(generate_number_pyramid(height))