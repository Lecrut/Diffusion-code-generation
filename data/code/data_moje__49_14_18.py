def render_square(side: int) -> str:
    line = "*" * side
    return "\n".join([line] * side)

if __name__ == "__main__":
    print(render_square(7))