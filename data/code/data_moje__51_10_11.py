def generate_number_pyramid(height):
    if height <= 0:
        return ""
    lines = []
    for row in range(1, height + 1):
        spaces = " " * (height - row)
        numbers = " ".join(str(num) for num in range(1, row + 1))
        lines.append(f"{spaces}{numbers}")
    return "\n".join(lines)

if __name__ == "__main__":
    print(generate_number_pyramid(5))