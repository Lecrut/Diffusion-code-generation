def build_diamond(n):
    if n <= 0:
        return ""
    half = n // 2 + 1
    result = []
    for i in range(half):
        spaces = " " * (half - 1 - i)
        stars = "*" * (2 * i + 1)
        result.append(spaces + stars)
    for i in range(half - 2, -1, -1):
        spaces = " " * (half - 1 - i)
        stars = "*" * (2 * i + 1)
        result.append(spaces + stars)
    return "\n".join(result)

if __name__ == "__main__":
    sample_size = 5
    print(build_diamond(sample_size))