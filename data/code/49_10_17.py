def generate_star_pattern(side_length):
    if not isinstance(side_length, int):
        raise TypeError("Side length must be an integer")
    if side_length < 1:
        raise ValueError("Side length must be positive")
    row = "*" * side_length
    return (row + "\n") * side_length

if __name__ == "__main__":
    result = generate_star_pattern(5)
    print(result.rstrip(), end="")
    print()