def print_square_pattern(side_length: int) -> str:
    if side_length <= 0:
        return ""
    star_line = "* " * side_length
    return (star_line.rstrip() + "\n") * side_length

if __name__ == "__main__":
    side = 5
    result = print_square_pattern(side)
    print(result, end="")