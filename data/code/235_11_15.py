DIAMOND_HEIGHT = 7

def render_diamond():
    lines = [
        "       *",
        "      ***",
        "     *****",
        "    *******",
        "   *********",
        "    *******",
        "     *****",
        "      ***",
        "       *"
    ]
    for line in lines:
        print(line)

if __name__ == '__main__':
    render_diamond()