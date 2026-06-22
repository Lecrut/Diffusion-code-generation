def render_star_square(side_length: int) -> str:
    return "\n".join(["* " * side_length for _ in range(side_length)])

if __name__ == "__main__":
    side = 7
    print(render_star_square(side))