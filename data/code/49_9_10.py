def print_star_square(size: int) -> str:
    row = "*" * size
    return "\n".join([row] * size)

if __name__ == '__main__':
    fixed_size = 12
    result = print_star_square(fixed_size)
    print(result)