def render_square(side_length):
    if side_length < 1:
        return ""
    pattern = ("*" * side_length + "\n") * side_length
    return pattern.rstrip("\n")

if __name__ == "__main__":
    sample_side = 7
    result = render_square(sample_side)
    print(result)