def generate_number_pyramid(height: int) -> str:
    lines = []
    for row in range(1, height + 1):
        spaces = " " * (height - row)
        numbers = " ".join(str(num) for num in range(1, row + 1))
        lines.append(f"{spaces}{numbers}")
    return "\n".join(lines)

if __name__ == "__main__":
    sample_height = 5
    print(generate_number_pyramid(sample_height))