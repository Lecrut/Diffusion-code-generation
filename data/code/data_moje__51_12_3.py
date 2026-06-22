def build_number_pyramid(size: int = 6) -> list[str]:
    return [" ".join(str(num) for num in range(1, row + 1)) for row in range(1, size + 1)]

if __name__ == '__main__':
    pyramid_lines = build_number_pyramid(6)
    print(pyramid_lines)