def render_diamond():
    diamond = [
        "   +   ",
        "  +++  ",
        " +++++ ",
        "+++++++",
        " +++++ ",
        "  +++  ",
        "   +   "
    ]
    for line in diamond:
        print(line)

if __name__ == '__main__':
    render_diamond()