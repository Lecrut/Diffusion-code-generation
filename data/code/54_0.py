def generate_hollow_square(size):
    if size <= 0:
        return ""
    if size == 1:
        return "*"
    result = ["*"] * size
    middle_lines = ["*"] + [" "] * (size - 2) + ["*"]
    middle_str = "".join(middle_lines)
    full_size = size
    for i in range(1, full_size - 1):
        result[i] = middle_str
    return "\n".join(result)

if __name__ == '__main__':
    print(generate_hollow_square(5))