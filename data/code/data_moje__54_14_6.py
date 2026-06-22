def render_hollow_square(size: int) -> str:
    if size <= 0:
        return ""
    if size == 1:
        return "*"
    first_row = "*" * size
    middle_row = "*" + " " * (size - 2) + "*"
    return "\n".join([first_row] + [middle_row] * (size - 2) + [first_row])

if __name__ == "__main__":
    sample_size = 5
    result = render_hollow_square(sample_size)
    print(result)