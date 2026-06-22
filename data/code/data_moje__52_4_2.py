def generate_diamond_pattern(center_width):
    result = []
    max_spaces = (center_width - 1) // 2
    for i in range(center_width):
        if i <= max_spaces:
            spaces = max_spaces - i
            stars = 2 * i + 1
            result.append(" " * spaces + "*" * stars)
        else:
            spaces = i - max_spaces
            stars = center_width - 2 * spaces
            result.append(" " * spaces + "*" * stars)
    return result

if __name__ == '__main__':
    pattern = generate_diamond_pattern(9)
    for line in pattern:
        print(line)