def render_star_square(side_length: int) -> str:
    if side_length <= 0:
        return ""
    row = "*" * side_length
    return "\n".join([row] * side_length)

if __name__ == "__main__":
    print(render_star_square(7))