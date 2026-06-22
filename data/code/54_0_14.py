def generate_hollow_square(size):
    if size <= 0:
        return ""
    if size == 1:
        return "*"
    result = []
    top_bottom = "*" * size
    middle = "*" + " " * (size - 2) + "*"
    result.append(top_bottom)
    for _ in range(size - 2):
        result.append(middle)
    result.append(top_bottom)
    return "\n".join(result)

if __name__ == "__main__":
    print(generate_hollow_square(5))
    print(generate_hollow_square(1))
    print(generate_hollow_square(3))