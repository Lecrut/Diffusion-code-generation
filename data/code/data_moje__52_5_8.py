def render_diamond():
    n = 3
    half = []
    for i in range(1, n + 1):
        half.append(" " * (n - i) + "* " * i)
    upper = half[:-1]
    lower = half[::-1]
    lines = upper + lower
    return "\n".join(lines)

if __name__ == "__main__":
    result = render_diamond()
    print(result)