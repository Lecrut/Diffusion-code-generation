def hollow_square(size: int) -> str:
    if size <= 0:
        return ""
    if size == 1:
        return "*"
    full_line = "*" * size
    mid_line = "*" + " " * (size - 2) + "*"
    return "\n".join([full_line] + [mid_line] * (size - 2) + [full_line])

if __name__ == '__main__':
    test_dimension = 7
    result = hollow_square(test_dimension)
    print(result)