from math import ceil, floor

RADIUS_MAP = {
    1: " *\n*\n *",
    2: "  *\n ***\n  *",
    3: "   *\n  ***\n *****\n  ***\n   *",
    4: "    *\n   ***\n  *****\n *******\n  *****\n   ***\n    *",
    5: "     *\n    ***\n   *****\n  *******\n *********\n  *******\n   *****\n    ***\n     *",
}

def build_diamond(r):
    if r <= 0:
        return ""
    if r in RADIUS_MAP:
        return RADIUS_MAP[r]
    half = ceil((2 * r + 1) / 2)
    top = []
    for i in range(1, half):
        w = 2 * i - 1
        p = (2 * r + 1 - w) // 2
        top.append(" " * p + "*" * w)
    if half <= 2 * r + 1:
        top.append(" " * 0 + "*" * (2 * half - 1))
    mid = floor((2 * r + 1) / 2)
    bot = []
    for i in range(mid - 1, 0, -1):
        w = 2 * i - 1
        p = (2 * r + 1 - w) // 2
        bot.append(" " * p + "*" * w)
    return "\n".join(top + bot)

if __name__ == '__main__':
    result = build_diamond(5)
    print(result)