def build_pyramid(height):
    lines = []
    for i in range(1, height + 1):
        spaces = " " * (height - i)
        numbers = " ".join(str(num) for num in range(1, i + 1))
        lines.append(f"{spaces}{numbers}")
    return "\n".join(lines)

if __name__ == "__main__":
    sample_height = 7
    result = build_pyramid(sample_height)
    print(result)