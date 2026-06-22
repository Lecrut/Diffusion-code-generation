def render_hollow_square(size: int) -> str:
    if size <= 0:
        return ""
    if size == 1:
        return "*"
    top_bottom = "*" * size
    middle = "*" + " " * (size - 2) + "*"
    return "\n".join([top_bottom] + [middle] * (size - 2) + [top_bottom])

if __name__ == '__main__':
    sample_size = 5
    print(render_hollow_square(sample_size))