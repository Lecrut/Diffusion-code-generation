def generate_diamond(size: int) -> str:
    if size <= 0:
        return ""
    result = []
    for i in range(1, size + 1):
        spaces = " " * (size - i)
        stars = "*" * (2 * i - 1)
        result.append(spaces + stars)
    for i in range(size - 1, 0, -1):
        spaces = " " * (size - i)
        stars = "*" * (2 * i - 1)
        result.append(spaces + stars)
    return "\n".join(result)

if __name__ == "__main__":
    print(generate_diamond(3))