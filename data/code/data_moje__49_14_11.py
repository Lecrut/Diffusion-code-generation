def render_square(side_length: int) -> str:
    if side_length <= 0:
        return ""
    if side_length == 1:
        return "*"
    row_full = "*" * side_length
    row_empty = "*" + " " * (side_length - 2) + "*"
    return "\n".join([row_full] + [row_empty] * (side_length - 2) + [row_full])

if __name__ == '__main__':
    result = render_square(7)
    print(result)