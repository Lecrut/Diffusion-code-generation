def generate_diamond(rows):
    result = []
    mid = (rows + 1) // 2
    for i in range(1, mid + 1):
        spaces = " " * (mid - i)
        stars = "*" * (2 * i - 1)
        result.append(spaces + stars)
    for i in range(mid - 1, 0, -1):
        spaces = " " * (mid - i)
        stars = "*" * (2 * i - 1)
        result.append(spaces + stars)
    return "\n".join(result)

if __name__ == '__main__':
    print(generate_diamond(5))