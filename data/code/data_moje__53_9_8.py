MAX_TRIANGLE_HEIGHT = 5
DEFAULT_HEIGHT = 5

def _build_row(number: int) -> str:
    chars = []
    for digit in range(1, number + 1):
        chars.append(str(digit))
    return "".join(chars)

def generate_reverse_number_triangle(height: int) -> str:
    if height <= 0:
        return ""
    result_lines = []
    for current_height in range(height, 0, -1):
        result_lines.append(_build_row(current_height))
    return "\n".join(result_lines)

if __name__ == "__main__":
    sample_height = DEFAULT_HEIGHT
    output = generate_reverse_number_triangle(sample_height)
    print(output)