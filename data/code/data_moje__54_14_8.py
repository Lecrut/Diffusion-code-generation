def render_hollow_square(size):
    if size <= 0:
        return ""
    if size == 1:
        return "*"
    top_bottom = "*" * size
    middle = "*" + " " * (size - 2) + "*"
    result = [top_bottom]
    for _ in range(size - 2):
        result.append(middle)
    result.append(top_bottom)
    return "\n".join(result)

if __name__ == '__main__':
    sample_size = 5
    print(render_hollow_square(sample_size))