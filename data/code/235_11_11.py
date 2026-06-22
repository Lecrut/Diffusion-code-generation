DIAMOND_PATTERNS = {
    1: " * ",
    2: "*   *\n ***",
    3: "*     *\n  ***\n   *",
    4: "*       *\n  ****\n   **\n    *",
    5: "*         *\n  *****\n   ***\n    *"
}

def render_diamond(n):
    print(DIAMOND_PATTERNS.get(n, "Invalid size"))

if __name__ == '__main__':
    diamond_size = 3
    render_diamond(diamond_size)