def create_hollow_square(size: int) -> list[str]:
    if size <= 0:
        return []
    if size == 1:
        return ["*"]
    edge = "*" * size
    middle = "*" + " " * (size - 2) + "*"
    return [edge] + [middle] * (size - 2) + [edge]

if __name__ == '__main__':
    square = create_hollow_square(10)
    for line in square:
        print(line)