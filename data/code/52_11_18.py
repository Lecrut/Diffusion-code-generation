def generate_diamond_star_pattern(size):
    result = []
    if size <= 0:
        return ""
    upper_part = []
    for i in range(1, size + 1):
        spaces = " " * (size - i)
        stars = "*" * (2 * i - 1)
        upper_part.append(spaces + stars)
    lower_part = []
    for i in range(size - 1, 0, -1):
        spaces = " " * (size - i)
        stars = "*" * (2 * i - 1)
        lower_part.append(spaces + stars)
    result.extend(upper_part)
    result.extend(lower_part)
    return "\n".join(result)

if __name__ == '__main__':
    sample_size = 5
    output = generate_diamond_star_pattern(sample_size)
    print(output)