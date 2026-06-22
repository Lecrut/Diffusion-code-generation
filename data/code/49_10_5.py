def print_star_square(side_length: int) -> str:
    if side_length <= 0:
        return ""
    line = "*" * side_length
    return "\n".join([line] * side_length)

if __name__ == "__main__":
    sample_side = 5
    result = print_star_square(sample_side)
    print(result)