def generate_hollow_square(size):
    if size <= 0:
        return ""
    if size == 1:
        return "*"
    if size == 2:
        return "**\n**"
    if size == 3:
        return "***\n* *\n***"
    result = []
    top_bottom = "*" * size
    result.append(top_bottom)
    middle_spaces = "*" + " " * (size - 2) + "*"
    for _ in range(size - 2):
        result.append(middle_spaces)
    result.append(top_bottom)
    return "\n".join(result)

if __name__ == '__main__':
    sample_size = 5
    print(generate_hollow_square(sample_size))